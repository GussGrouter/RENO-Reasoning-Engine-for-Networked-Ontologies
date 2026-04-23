# network-algorithmics-13-18-5-load-balanced-switching (chunk 000001)

# Network Algorithmics — 13.18.5 Load-balanced switching (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 401
- Slice: from `13.18.5 Load-balanced switching` up to next detected section heading

---

13.18.5 Load-balanced switching
LBS (Chang et al., 2002a,b; Ding et al., 2014; Jaramillo et al., 2008; Keslassy, 2004; Lin and Keslassy,
2010; Yang et al., 2017a,b), first introduced by Chang et al. (2002a,b), and later further developed by
others (e.g. Ding et al., 2014; Jaramillo et al., 2008; Keslassy, 2004; Lin and Keslassy, 2010; Yang et
al., 2017a), is another approach to scaling to larger and faster switches. It does so by removing one
of the two aforementioned major hurdles to scaling: whereas in a Clos network, bipartite matching
computations are still needed in each small switch, in LBS they are completely avoided.
     LBS architectures build upon the idea of Valiant load balancing (Leslie, 1982), which predated the
design of any IP switch or router. They rely on two switching stages for routing packets. Fig. 13.21
shows a diagram of a generic two-stage load-balanced switch. The first switching stage connects the
first stage of input ports to the center stage of intermediate ports, and the second switching stage con-
nects the center stage of intermediate ports to the final stage of output ports. Each switching stage
executes a predetermined periodic sequence (hence, no bipartite matching computations are needed!)
of connection patterns such that each input is connected to each output of a switching stage N1 th of the
time.
     A typical connection pattern for LBS is the cyclic shifts. For example, the following is a standard
cyclic-shift connection pattern that is easy to understand and verify. The first switching fabric executes
a periodic “increasing” sequence of matchings: at any time slot t, each input port i is connected to
the intermediate port (i + t) mod N . It has been shown in Chang et al. (2002a) that, when the traffic
arrival process satisfies certain mild stationarity conditions, this periodic sequence of matchings can
spread the incoming traffic very evenly across all intermediate ports. The second switching fabric, on

13.19 Scaling to faster link speeds                 375

the other hand, will execute a periodic “decreasing” sequence of matchings: at any time slot t, each
intermediate port i is connected to the output port (i − t) mod N .
     Although the basic load-balanced switch originally proposed in Chang et al. (2002a) is capable of
achieving 100% throughput, it has a serious problem that packet departures can be badly out of order.
In the basic load-balanced switch consecutive packets at an input port are spread to all N intermediate
ports upon arrival. Packets going through different intermediate ports may encounter different queueing
delays. Thus some of these packets may arrive at their output ports out-of-order. This is detrimental
to Internet traffic since the widely used TCP transport protocol falsely regards out-of-order packets as
indications of congestion and packet loss. Therefore a number of solutions (Ding et al., 2014; Yang et
al., 2017a,b) have been proposed to address this problem.
