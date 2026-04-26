# network-algorithmics-15-6-exercises-1-fcvc-flow-control-protocol-the-fcvc-flow-control-protocol-of (chunk 000004)

The goal of this chapter is to argue the contrary: that measurement at high speeds is difficult because
of resource limitations and lack of built-in support; that the problems will only grow worse as ISPs
abandon their current generation of links for even faster ones; and that algorithmics can provide exciting
alternatives to the measurement quandary by focusing on how measurements will ultimately be used.
To develop this theme, it is worth understanding right away why the general problem of measurement
is hard and why even the specific problem of packet counting can be difficult.
    This chapter is organized as follows. Section 16.1 describes the challenges involved in measurement.
Section 16.2 shows how to reduce the required width of an SRAM counter using a DRAM backing-
store and introduces two different schemes, both of which are deterministic algorithms, for that purpose.
Section 16.3 describes a randomized algorithm for the same purpose that is much simpler and much
more SRAM-efficient. These three counter schemes all implement passive counters, in which counters
need to handle increments, but not read accesses, in real time.
    Section 16.4 describes an SRAM-efficient scheme called BRICK for maintaining active counters
that need to handle both in real time. In network measurement applications each counter is associated
with a traffic flow, and the value of the counter is a special and very simple type of state information
associated with the flow. Section 16.5 describes an extension of BRICK for efficiently maintaining
general state information for many traffic flows.
    Section 16.6 details a different technique for reducing counter widths by using randomized counting,
which trades accuracy for counter width. Section 16.7 presents a different approach to reducing the
number of counters required (as opposed to the width) by keeping track of counters only above a
threshold. Section 16.8 shows how to reduce the number of counters even further for some applications
by counting only the number of distinct flows.
    Techniques in prior sections require computation on every packet. Section 16.9 takes a different
tack by describing the sampled NetFlow technique for reducing packet processing; in NetFlow only a
random subset of packets is processed to produce either a log or an aggregated set of counters. Sec-
tion 16.10 shows how to reduce the overhead of shipping NetFlow records to managers. Section 16.11
explains how to replace the independent sampling method of NetFlow with a consistent sampling tech-
nique in all routers that allow packet trajectories to be traced.
    The next three sections of the chapter move to a higher-level view of measurement. In Section 16.12
we describe a solution to the accounting problem. This problem is of great interest to ISPs, and the
solution method is in the best tradition of the systems approach advocated throughout this book. In
Section 16.13 we describe a solution to the traffic matrix problem using the same concerted systems
approach. Section 16.14 presents a very different approach to measurement, called passive measure-
ment, that treats the network as a black box. It includes an example of the use of passive measurement
to compute the loss rate to a Web server.
    The last six sections of this chapter provide a small sample of a fascinating new algorithmic tool
to network measurement that has been developed mostly in the new millennium: data streaming and
sketching algorithms (Muthukrishnan, 2005). These algorithms can, among other things, generate more
informative and hence better traffic logs for a variety of measurement tasks. Section 16.15 provides a
brief introduction to the data streaming model and the design objectives of data streaming algorithms.
Section 16.16 revisits the counting of the number of distinct flows from a new data-streaming perspec-
tive. One such data-streaming algorithm, called min-hash sketch, leads to an unexpected solution to a
classical database problem called associative-rule mining.

16.1 Why measurement is hard                        451
