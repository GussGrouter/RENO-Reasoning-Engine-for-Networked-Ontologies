# network-algorithmics-13-3-router-history-from-buses-to-crossbars (chunk 000002)

sending bits on the bus. Other electrical effects include those caused by multiple connectors (from each
line card) and reflections on the line (McKeown, 1997).
    The classical way to get around this bottleneck is to use a crossbar switch, as shown in Fig. 13.2(D).
A crossbar switch essentially has a set of 2N parallel buses, one bus per source line card and one bus
per destination line card. If one thinks of the source buses as being horizontal and the destination buses
as being vertical, the matrix of buses forms what is called a crossbar.
    Potentially, this provides an N -fold speedup over a single bus because, in the best case, all N buses
will be used in parallel at the same time to transfer data, instead of a single bus. Of course, to get this
speedup requires finding N disjoint source–destination pairs at each time slot. Trying to get close to
this bound is the major scheduling problem studied in this chapter.
    Although they do not necessarily go together, another design change that accompanied crossbar
switches designed between 1995 and 2002 is the use of special-purpose integrated circuits (ASICs)
as forwarding engines instead of general-purpose CPUs. These forwarding engines are typically faster
(because they are designed specifically to process Internet packets) and cheaper than general-purpose
CPUs. Two disadvantages of such forwarding engines include design costs for each such ASIC and the
lack of programmability (which makes changes in the field difficult or impossible). These problems
have again led to proposals for faster, but yet programmable, network processors (see Chapter 2).

13.4 The take-a-ticket crossbar scheduler               337

FIGURE 13.3
Basic crossbar switch.
