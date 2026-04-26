# Network Algorithmics — 14.16.1 Random aggregation The idea behind SFQ (McKenney, 1991) is to employ Principle P3a by trading certainty in fairness for (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 452
- Slice: from `14.16.1 Random aggregation The idea behind SFQ (McKenney, 1991) is to employ Principle P3a by trading certainty in fairness for` up to next detected section heading

---

14.16.1 Random aggregation
The idea behind SFQ (McKenney, 1991) is to employ Principle P3a by trading certainty in fairness for
reduced state. In this proposal backbone routers keep a fixed set of flow queues that is affordable, say,
125,000, on which they do, say, DRR. When packets arrive, some set of packet fields (say, destination,
source, and the destination and source ports for TCP and UDP traffic) are hashed to a flow queue. Thus
assuming that a flow is defined by the set of fields used for hashing, a given flow will always be hashed
to the same flow queue. Thus with 250,000 concurrent flows and 125,000 flow queues, roughly 2 flows
will share the same flow queue or hash bucket.
    Stochastic fair queuing has two disadvantages. First, different backbone routers can hash flows into
different groups because routers need to be able to change their hash function if the hash distributes
unevenly. Second, SFQ does not allow some flows to be treated differently (either locally within one
router or globally across routers) from other flows, a crucial feature for QoS. Thus SFQ only provides
some sort of scalable and uniform bandwidth fairness.
