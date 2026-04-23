# network-algorithmics-14-16-scalable-fair-queuing (chunk 000001)

# Network Algorithmics — 14.16 Scalable fair queuing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 451
- Slice: from `14.16 Scalable fair queuing` up to next detected section heading

---

14.16 Scalable fair queuing
Using multiple queues for each flow, we have seen that: (1) A constant-time algorithm (DRR) can pro-
vide bandwidth guarantees for QoS even using software and (2) a logarithmic time-overhead algorithm
can provide bandwidth and delay guarantees; further, the logarithmic overhead can be made negligible
using extra hardware to implement a priority queue. Thus it would seem that QoS is easy to implement
in routers ranging from small edge routers to the bigger backbone (core) routers.
    Unfortunately, even very old studies by Thompson et al. (1997) of backbone routers show there
to be around 250,000 concurrent flows. With increasing traffic, we expect this number to grow to a
million and possibly larger as Internet speed and traffic increase. Keeping state for a million flows can
be a difficult task in backbone routers. If the state is kept in SRAM, the amount of memory required
can be expensive; if the state is kept in DRAM, state lookup could be slow.
    More cogently, advocates of Internet scaling and aggregation point out that Internet routing currently
uses only around 1,000,000 prefixes for over a billion nodes. Why should QoS require so much state
when none of the other components of IP do? In particular, while the QoS state may be manageable
today, it might represent a serious threat to the scaling of the Internet. Just as prefixes aggregate routes
for multiple IP addresses, is there a way to aggregate flow state?
    Aggregation implies that backbone routers will treat groups of flows in identical fashion. Aggre-
gation requires that: (1) It must be reasonable for the members of the aggregated group to be treated
identically and (2) there must be an efficient mapping from packet headers to aggregation groups. For

14.16 Scalable fair queuing           425

example, in the case of IP routing: (1) A prefix aggregates a number of addresses that share the same
output link, often because they are in the same relative geographic area, and (2) the longest matching
prefix provides an efficient mapping from destination addresses in headers to the appropriate prefix.
    There are three interesting proposals to provide aggregated QoS, which we describe briefly: random
aggregation (stochastic fair queueing (SFQ)); aggregation at the network edge (DiffServ); and aggre-
gation at the network edge together with efficient policing of misbehaving flows (core stateless fair
queuing).
