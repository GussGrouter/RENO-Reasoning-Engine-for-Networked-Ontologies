# network-algorithmics-14-16-3-edge-aggregation-with-policing (chunk 000001)

# Network Algorithmics — 14.16.3 Edge aggregation with policing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 453
- Slice: from `14.16.3 Edge aggregation with policing` up to next detected section heading

---

14.16.3 Edge aggregation with policing
Using edge aggregation, two flows (say, F 1 and F 2) that have reserved bandwidth (say, B1 and B2 ,
respectively) could be aggregated into a class that has nominally reserved some bandwidth, which is
B ≥ B1 + B2 for all flows in the class. Consider Fig. 14.24. Suppose F 1 decides to oversubscribe and to
send at a rate greater than B. The edge router ER in Fig. 14.24 may currently have sufficient bandwidth
to allow all packets of flow F 1 and F 2 through. Unfortunately, when this aggregated class reaches the
backbone (core) router CR, suppose the core router is limited in bandwidth and must drop packets.
Ideally, CR should only drop oversubscribed flows like F 1 and let all of F 2’s packets through.
    How, though, can CR tell which flows are oversubscribed? It could do so by keeping state for all
flows passing through, but that would defeat scaling. A clever idea, called core-stateless fair queuing
(Stoica et al., 1998), makes the observation that the edge router ER has sufficient information to distin-
guish the oversubscribed flows. Thus ER can, using Principle P10, pass information in packet headers
to CR.
    How, though, should CR handle oversubscribed flows? Dropping all such marked packets may be
too severe. If there is enough bandwidth for some oversubscribed flows, it seems reasonable for CR to
drop in proportion to the degree a flow is oversubscribed. Thus ER should pass a value in the packet
header of a flow that is proportional to the degree a flow is oversubscribed. To implement this idea, CR
can drop randomly (P3a), with a drop probability that is proportional to the degree of oversubscription.
While this has some error probability, it is close enough. Most importantly, random dropping can be
implemented without CR keeping any state per flow. In effect, CR is implementing RED, but with the
drop probability computed based on a packet header field set by an edge router.
    While core-stateless is a nice idea, we note that unlike SFQ (which can be implemented in isola-
tion without cooperation between routers) and DiffServ (which has mustered sufficient support for its
standardized use of the TOS field), core-stateless fair queuing is, as of now, only a research proposal
(Stoica et al., 1998).

14.17 Summary
In this chapter we attacked another major implementation bottleneck for a router: scheduling data pack-
ets to reduce the effects of congestion and to provide fairness and QoS guarantees to certain flows. We

14.18 Exercises           427
