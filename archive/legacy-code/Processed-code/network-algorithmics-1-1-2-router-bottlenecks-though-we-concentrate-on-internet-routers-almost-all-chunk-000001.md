# network-algorithmics-1-1-2-router-bottlenecks-though-we-concentrate-on-internet-routers-almost-all (chunk 000001)

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
