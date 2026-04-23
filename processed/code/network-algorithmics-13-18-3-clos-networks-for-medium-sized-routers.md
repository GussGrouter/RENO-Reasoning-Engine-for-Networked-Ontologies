# Network Algorithmics — 13.18.3 Clos networks for medium-sized routers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 393
- Slice: from `13.18.3 Clos networks for medium-sized routers` up to next detected section heading

---

13.18.3 Clos networks for medium-sized routers
Despite the lack of current focus on crosspoints in VLSI technology, our survey of scalable fabrics
for routers begins by looking at the historically earliest proposal for a scalable switch fabric. Charles
Clos first proposed his idea in 1955 to reduce the expense of electromechanical switching in telephone
switches. Fortunately, the design also reduces the number of components and links required to connect
up a number of smaller switches. It is thus useful in a present-day context. Specifically, a Clos network
appears to be used in the Juniper Networks T-series multichassis router product, introduced 47 years
later, in 2002.
    The basic Clos network uses a simple divide-and-conquer (P15) approach to reducing crosspoints
by switching in three stages, as shown in Fig. 13.16. The first stage divides the N total inputs into
groups of n inputs each, and each group of n inputs is switched to the second stage by a small (n-by-k)
switch. Thus there are N/n “small” switches in the first stage.
    The second stage consists of k switches, each of which is an N/n-by-N/n switch. Each of the
k outputs of each first-stage switch is connected in order to all the k second-stage switches. More
precisely, output j of switch i in the first stage is connected to input i of switch j in the second stage.
The third stage is a mirror reversal of the first stage, and the interconnections between the second and
third stages are also the mirror reversal of those between the first and second stages. The view from

                                             13.18 Scaling to larger and faster switches               367



outputs leftward to the middle stage is the same as the view from inputs to the middle stage. More
precisely, each of the N/n outputs of the first stage is connected in order to the inputs of the third stage.
    A switch is said to be nonblocking if, whenever the input and output are free, a connection can be
made through the switch using free resources. Thus a crossbar is always nonblocking by selecting the
crosspoint corresponding to the input–output pair, which is never used for any other pair. On the other
hand, in Fig. 13.16 every input switch has only k connections to the middle stage, and every middle
stage has only one path to any particular switch in the third stage. Thus for small k, it is easily possible
to block a new connection because there is no path from an input I to a middle-stage switch that has a
free line to an output O.

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



    What happens to a Clos network when k reduces from 2n − 1 to n? If k = n, the Clos network is
no longer nonblocking. Instead, the Clos network becomes what is called rearrangeably nonblocking.
In other words, the new input i can be connected to o as long as it’s possible to rearrange some of
the existing connections between inputs and outputs to use different middle-stage switches. A proof
and possible switching algorithm is described in Appendix A. It can be safely skipped by readers
uninterested in the theory.
    The bottom line behind all the math in Section A.3.1 in Appendix A is as follows. First, k = n is
clearly much more economical than k = 2n − 1 because it reduces the number of middle-layer switches
by a factor of two. However, while the Clos network is rearrangeably nonblocking, deterministic edge-
coloring algorithms for switch scheduling appear at this time to be quite complex. Second, the matching
proof for telephone calls assumes that all calls appear at the inputs at the same time; when a new call
arrives, existing calls have to be potentially rearranged to fit the new routes.

Clos networks and multichassis routers
Whereas the Clos network is required to be nonblocking or at least rearrangeably nonblocking for it
to be used for a telephone network, there is no such requirement for it to be used for a multichassis
router (i.e., a packet switch), due to a key difference between the two applications: a telephone switch
has no buffer, whereas a (small) packet switch does. Roughly speaking, requiring a Clos network to
be nonblocking, or rearrangeably nonblocking, equates to requiring it to achieve perfect load-balance
among the intermediate switches during every time slot, which is necessary where there is no buffering.

                                             13.18 Scaling to larger and faster switches              369



Where there is buffering, however, this load-balance needs only to be statistically perfect, a notion that
we will make precise next.
    We now construct a large switch that is perfectly load-balanced statistically, using a three-stage Clos
network of small switches with buffers. In this construction we make k = n as previously explained,
so that there are n switches
                        √       in each stage.√Since √N = n2 , in this case, we have pieced together an
N × N switch using 3 N switches of size N × N. For example, when N = 1024, we use only 96
switches of size 32 × 32 to build a giant 1024 × 1024 switch. We will show that, in this three-stage Clos
network, there is no need to compute matchings (every time slot) for this giant 1024 × 1024 bipartite
graph. Instead, each small switch computes matchings for its 32 × 32 bipartite graph, which is much
easier computationally.
    In this three-stage Clos network statistically perfect load-balancing can be achieved using the fol-
lowing simple randomized strategy. In this strategy each switch in the first stage statistically evenly
distributes all its incoming packets to all n switches in the second stage. Then, at each switch in the
second stage, every incoming packet has to be forwarded to the third stage switch where the destination
output port is located. This will not cause load imbalance at the second stage since it can be shown that,
if every switch in the first stage does a perfect job of statistical load-balancing, then, at each switch in
the second stage, there is a statistically equal amount of traffic destined for every output port of it. For
a similar reason, there will be no load imbalance at the third stage.
    Then, how can every switch in the first stage do a perfect job of statistical load-balancing? This can
be achieved by the following simple and intuitive scheme, with a caveat that will be explained shortly.
We describe only the operations of a single switch at the first level because operations at any other
switch are identical; in this switch we consider only the operations at a single-input port, as operations
at other input ports are identical. The scheme is, for every incoming packet, this input port simply
forwards it to an output port, and correspondingly a switch at the second level, that is chosen uniformly
at random.
    The caveat with this scheme is that, because load balancing is performed on a packet-by-packet basis
(i.e., at the packet level), two consecutive packets that belong to the same TCP flow may go through
two different switches at the second stage and experience different queueing delays. As a result, they
may depart from the (same) switch at the third stage and arrive at their destination out of order. Such
out-of-order packet arrivals could unnecessarily decrease the throughput of the TCP flow since the
TCP clients (on both ends) can mistakenly interpret them as an indication of packet losses caused by
network congestion, and respond accordingly (e.g., by reducing the size of congestion window). This
was generally not an issue in the dot.com era, when the average data rate provided to a TCP flow was
typically quite low (typically tens to hundreds of Kbps), which would not be much further reduced
by this packet reorder problem. Indeed, it appears that Juniper adopted a similar packet-level load
balancing scheme in the early 2000s, although it’s not possible to be sure about what Juniper actually
did because their documentation is (probably intentionally) vague.
    In recent years, three-stage Clos networks have mostly been used instead to build a large data center
network (which can be viewed as a giant switch) (Loukissas et al., 2008; Cao et al., 2013; Ghorbani
et al., 2017; Zhao et al., 2019). However, as the data rates of TCP flows nowadays are much higher,
especially in a data center network, this packet-reorder problem can no longer be ignored. Hence, all
recent packet-based load-balancing solutions for three-stage Clos networks have to either eliminate
or mitigate this packet reorder problem. For example, in Ghorbani et al. (2017) the built-in packet

370      Chapter 13 Switching



re-sequencing capability of modern NICs at end hosts is cleverly exploited to keep the percentage of
out-of-order packets to a minimum.
    An alternative load-balancing approach, known as TCP hashing (Keslassy, 2004), does not have
this packet reorder problem. In this approach all packets belonging to the same TCP flow must take the
same path (i.e., links and switches) through the Clos network. At each input port of a switch at the first
level, this can be achieved by hashing on the TCP flow identifier (source and destination IP addresses,
source and destination ports, and protocol identification) of every incoming packet to obtain a value
between 1 and N , which corresponds to the output port of this switch to which this packet should be
forwarded. However, while eliminating the packet-reorder problem, TCP hashing can lead to severe
load-imbalance. For example, all packets in an elephant flow, which travel the same path, will congest
the links and switches along the path. Hence, recently, in an LBS scheme (to be described in Sec-
tion 13.18.5) called safe randomized switching (SRS) (Yang et al., 2017b), the TCP hashing approach
was enhanced with two safety mechanisms to effectively mitigate this load-imbalance problem.
