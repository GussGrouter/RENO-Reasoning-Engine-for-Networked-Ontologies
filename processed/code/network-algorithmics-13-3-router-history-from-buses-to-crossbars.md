# Network Algorithmics — 13.3 Router history: from buses to crossbars (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 362
- Slice: from `13.3 Router history: from buses to crossbars` up to next detected section heading

---

13.3 Router history: from buses to crossbars
Router switches have evolved from the simplest shared-medium (bus or memory) switches, shown in
part A of Fig. 13.2, to the more modern crossbar switches, shown in part D of Fig. 13.2. A line card in a
router or switch contains the interface logic for a data link, such as a fiber-optic line or an Ethernet. The
earliest switches connected all the line cards internally via a high-speed bus (analogous to an internal
local area network) on which only one pair of line cards can communicate at a time. Thus if Line Card
1 is sending a packet to Line Card 2, no other pair of line cards can communicate.
    What is worse, in more ancient routers and switches, the forwarding decision was relegated to a
shared, general-purpose CPU. General-purpose CPUs allow for simpler and easily changeable for-
warding software. However, general-purpose CPUs were often slow because of the extra levels of
interpretation of general-purpose instructions. They also lacked the ability to control real-time con-
straints on packet processing because of nondeterminism due to mechanisms such as caches. Note also
that each packet traverses the bus twice, once to go to the CPU and once to go from the CPU to the
destination. This is because the CPU is on a separate card reachable only via the bus.
    Because the CPU was a bottleneck, a natural extension was the addition of a group of shared CPUs
for forwarding, any of which can forward a packet. For example, one CPU can forward packets from
Line Cards 1 through 3, the second from Line Cards 4 through 6, and so on. This increases the overall
throughput or reduces the performance requirement on each individual CPU, potentially leading to a
lower-cost design. However, without care it can lead to packet misordering, which is undesirable.
    Despite this, the bus remains a bottleneck. A single shared bus has speed limitations because of the
number of different sources and destinations that a single shared bus has to handle. These sources and
destinations add extra electrical loading that slows down signal rise times and ultimately the speed of

336       Chapter 13 Switching




FIGURE 13.2
Evolution of network switches, from shared-bus switches with a shared CPU to crossbar switches with a dedicated
forwarding engine per line card.


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
