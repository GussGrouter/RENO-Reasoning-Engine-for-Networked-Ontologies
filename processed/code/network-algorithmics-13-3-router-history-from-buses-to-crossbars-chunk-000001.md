# network-algorithmics-13-3-router-history-from-buses-to-crossbars (chunk 000001)

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
