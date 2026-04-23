# Network Algorithmics — 13.1 Router versus telephone switches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 360
- Slice: from `13.1 Router versus telephone switches` up to next detected section heading

---

13.1 Router versus telephone switches
Given our initial analogy to telephone switches, it is worthwhile outlining the major similarities and
differences between telephone and router switches. Early routers used a simple bus to connect input
and output links. A bus (Chapter 2) is a wire that allows only one input to send to one output at a time.
Today, however, almost every core router uses an internal crossbar that allows disjoint link pairs to
communicate in parallel, to increase effective throughput. Once again, the electronics plays the role of
the operator, activating transistor switches that connect input links to output links.
    In telephony a phone connection typically lasts for seconds if not for minutes. However, in Internet
switches each connection lasts for the duration of a single packet. This is 8 nanoseconds for a 40-byte
packet at 40 Gbps. Recall that caches cannot be relied upon to finesse lookups because of the rarity of
large trains of packets to the same destination. Similarly, it is unlikely that two consecutive packets at
a switch input port are destined to the same output port. This makes it hard to amortize the switching
overhead over multiple packets.
    Thus to operate at wire speed, the switching system must decide (i.e., compute) which input and
output links should be matched in a minimum packet arrival time. This makes the control portion of an
Internet switch (that sets up connections) much harder to build than a telephone switch. To simplify the

334      Chapter 13 Switching



       Table 13.1 Principles used in the various switches studied in this chapter.
       Number                            Principle                                   Switch
        P5b               Widen memory access for bandwidths                        Datapath
        P13                 Distribute queue control via tickets                   GigaSwitch
         P5a           Schedule outputs and hunt groups in parallel
        P11           Optimize for at most k < N output contention                 Knockout
        P15         Use tree of randomized concentrators for fairness
         P3                  Relax output buffer specification
        P13                    Use per-output input queues                           AN-2
        P14              N 2 communication feasible for small N
        P15                 Use randomized iterative matching
        P14         PPEs for round-robin fairness feasible for small N               iSLIP
         P3           Relax specification of grant-accept dependency
         P3a                      Trade certainty for time                     Sample-and-compare
        P12a  Compute matching incrementally from the recently used matching        SERENA
        P14                             Use bitmaps                              FFA in SW-QPS
        P15           Use a three-stage Clos network to reduce costs              Juniper T640
        P3b       Randomize load distribution to reduce k from 2n to n
        P15         Use a (log N)-stage Benes network to reduce costs             Growth fabric
         P3a               Use fast randomized routing scheme
        P15             Use a copy-twice multicast and binary tree
        P13                   Lay out grid using short wires                       Avici TSR



problem, most routers internally segment variable-sized packets into fixed-sized cells before sending to
the switch fabric. Mathematically, the switching component of a router reduces to solving a bipartite
matching problem: the router must match, in a fixed cell arrival time (time slot), input links with output
links to the maximum extent, the precise meaning of which will be elaborated in Section 13.8. While
“good” algorithms for bipartite matching are well known to run in milliseconds, solving the same
problem every 8 nanoseconds at 40 Gbps requires some systems thinking.
    For example, the solutions described in this chapter will trade accuracy for time (P3b), use hardware
parallelism (P5) and randomization (P3a), and exploit the fact that typical switches have 32–64 ports
to build fast priority queue operations using bitmaps (P14).
