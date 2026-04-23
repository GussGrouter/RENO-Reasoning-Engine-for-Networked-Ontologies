# Network Algorithmics — 1.1.2 Router bottlenecks Though we concentrate on Internet routers, almost all the techniques described in this book apply (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 32
- Slice: from `1.1.2 Router bottlenecks Though we concentrate on Internet routers, almost all the techniques described in this book apply` up to next detected section heading

---

1.1.2 Router bottlenecks
Though we concentrate on Internet routers, almost all the techniques described in this book apply
equally well to any other network devices, such as bridges, switches, gateways, monitors, and security
appliances, and to protocols other than IP, such as FiberChannel.
    Thus throughout the rest of the book, it is often useful to think of a router as a “generic network in-
terconnection device.” Unlike endnodes, these are special-purpose devices devoted to networking. Thus
there is very little structural overhead within a router, with only the use of a very lightweight operat-
ing system and a clearly separated forwarding path that often is completely implemented in hardware.
Instead of structure, the fundamental problems faced by routers are caused by scale and services.
• Scale: Network devices face two areas of scaling: bandwidth scaling and population scaling. Band-
  width scaling occurs because optical links keep getting faster, as the progress from 1-Gbps to
  40-Gbps links shows, and because Internet traffic keeps growing due to a diverse set of new ap-
  plications. Population scaling occurs because more endpoints get added to the Internet as more
  enterprises go online.
• Services: The need for speed and scale drove much of the networking industry in the 1980s and
  1990s as more businesses went online (e.g., Amazon.com) and whole new online services were cre-
  ated (e.g., eBay). But the very success of the Internet requires careful attention in the next decade
  to make it more effective by providing guarantees in terms of performance, security, and reliability.
  After all, if manufacturers (e.g., Dell) sell more online than by other channels, it is important to pro-
  vide network guarantees—delay in times of congestion, protection during attacks, and availability
  when failures occur. Finding ways to implement these new services at high speeds will be a major
  challenge for router vendors in the next decade.
    Fig. 1.2 previews the main router (bridge/gateway) bottlenecks covered in this book, together with
causes and solutions.
    First, all networking devices forward packets to their destination by looking up a forwarding table.
The simplest forwarding table lookup does an exact match with a destination address, as exemplified by
bridges. Chapter 10 describes fast and scalable exact-match lookup schemes. Unfortunately, population
scaling has made lookups far more complex for routers. To deal with large Internet populations, routers
keep a single entry called a prefix (analogous to a telephone area code) for a large group of stations.
Thus routers must do a more complex longest-prefix-match lookup. Chapter 11 describes solutions to
this problem that scale to increasing speeds and table sizes.

6         Chapter 1 Introducing network algorithmics




FIGURE 1.2
Preview of router bottlenecks, solutions to which are described in Parts 3 and 4 of the book.


    Many routers today offer what is sometimes called service differentiation, where different packets
can be treated differently in order to provide service and security guarantees. Unfortunately, this re-
quires an even more complex form of lookup called packet classification, in which the lookup is based
on the destination, source, and even the services that a packet is providing. This challenging issue is
tackled in Chapter 12.
    Next, all networking devices can be abstractly considered as switches that shunt packets coming in
from a set of input links to a set of output links. Thus a fundamental issue is that of building a high-
speed switch. This is hard, especially in the face of the growing gap between optical and electronic
speeds. The standard solution is to use parallelism via a crossbar switch. Unfortunately, it is nontrivial
to schedule a crossbar at high speeds, and parallelism is limited by a phenomenon known as head-of-
line blocking. Worse, population scaling and optical multiplexing are forcing switch vendors to build
switches with a large number of ports (e.g., 256), which exacerbates these other problems. Solutions to
these problems are described in Chapter 13.
    While the previous bottlenecks are caused by scaling, the next bottleneck is caused by the need for
new services. The issue of providing performance guarantees at high speeds is treated in Chapter 14,
where the issue of implementing so-called QoS (quality of service) mechanisms is studied. Chapter 15
briefly surveys another bottleneck that is becoming an increasing problem: the issue of bandwidth
within a router. It describes sample techniques, such as striping across internal buses and chip-to-chip
links.

                                               1.2 The techniques: network algorithmics                      7



    The final sections of the book take a brief look at emerging services that must, we believe, be part of
a well-engineered Internet of the future. First, routers of the future must build in support for measure-
ment, because measurement is the key to engineering networks to provide guarantees. While routers
today provide some support for measurement in terms of counters and NetFlow records, Chapter 16
also considers more innovative measurement mechanisms that may be implemented in the future.
    Chapter 17 describes security support, some of which is already being built into routers. Given the
increased sophistication, virulence, and rate of network attacks, we believe that implementing security
features in networking devices (whether routers or dedicated intrusion prevention/detection devices)
will be essential. Further, unless the security device can keep up with high-speed links, the device may
miss vital information required to spot an attack.
