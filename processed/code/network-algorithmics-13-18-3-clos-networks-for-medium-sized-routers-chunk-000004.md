# network-algorithmics-13-18-3-clos-networks-for-medium-sized-routers (chunk 000004)

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
