# network-algorithmics-10-5-exercise-1-arp-caches-another-example-of-an-exact-match-lookup-is-furnis (chunk 000002)

Consider a flight database in London that lists flights to a thousand US cities. One alternative would
be to keep a record specifying the path to each of the 1000 cities. Suppose, however, that most flights
to America hub through Boston, except flights to California, which hub through Los Angeles. This
observation can be exploited to reduce the flight database from a thousand entries to two prefix entries
(USA* → Boston; USA.CA.* → LA).
    A problem with this reduction is that a destination city like USA.CA.Fresno will now match both the
USA* and USA.CA.* prefixes; the database must return the longest match (USA.CA.*). Thus prefixes
have been used to compress a large database but at the cost of a more complex longest-matching-prefix
lookup.
    As described in Chapter 2 the Internet uses the same idea. In the year 2022 core routers stored only
around 900,000 prefixes instead of potentially billions of entries for each possible Internet address. For
example, to a core router, all the computers within a university, such as UCLA (University of California,
Los Angeles), will probably be reachable by the same next hop. If all the computers within UCLA are
given the same initial set of bits (the network number or prefix), then the router can store one entry for
UCLA instead of thousands of entries for each computer in UCLA.
    The world has changed significantly since the first edition as follows.
• Prefix Growth: Since the first edition, the core routing table has grown from around 150,000 in 2004
  to around 900,000 prefixes in 2022.
• IP v6: When the first edition was written, 128-bit IPv6 was being talked about but did not penetrate
  significantly because of the prevalence of Network Address Translation (NAT) boxes. However, the
  popularity of mobile and Internet of Things (IoT) devices have led to rapid deployment of IPv6,
  with IPv6 availability of Google users at over 30% (Google, 2022).
• DRAM versus SRAM: Many router hardware lookups find it cheaper to use a small amount of on-
  chip memory and large low-latency external DRAM instead of SRAM.
• Programmable Chips with TCAM: Chips, such as Intel’s Tofino-3 (Intel Corporation, 2022), have
  emerged that have a fairly large amount of TCAM and are programmable. While IP lookups can be
  done using TCAM, new data structures can use TCAM to scale to larger databases. Further, they
  can be programmed to do different IP lookup schemes using a new higher level language for router
  programming called P4 (P4 Open Source Programming Language, 2022).
• Software Defined Networks (SDN): The SDN movement allows the control plane (and with pro-
  grammable chips, even the data plane) to be changed by a centralized controller. Each router simply
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00018-X
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                     249

250      Chapter 11 Prefix-match lookups
