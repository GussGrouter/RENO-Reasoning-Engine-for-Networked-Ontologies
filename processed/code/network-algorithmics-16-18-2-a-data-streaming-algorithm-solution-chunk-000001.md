# network-algorithmics-16-18-2-a-data-streaming-algorithm-solution (chunk 000001)

# Network Algorithmics — 16.18.2 A data streaming algorithm solution (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 511
- Slice: from `16.18.2 A data streaming algorithm solution` up to next detected section heading

---

16.18.2 A data streaming algorithm solution
As explained earlier in Section 16.15, a naive solution to this problem is to use a hash table of per-flow
counters to keep track of all active flows, but the naive solution cannot scale to high link speeds at
a reasonable cost. Another possible approach (Duffield et al., 2003) is to sample a small percentage
of packets and then infer the flow distribution from the sampled traffic. The algorithm proposed in
Duffield et al. (2003) may well be the best algorithm in getting as much information as possible from
the sampled data. However, its accuracy is limited by the typically low sampling rate (e.g., 0.2%)
required to make the sampling operation affordable. The work by Hohn and Veitch (2003) has provided
theoretical insights into the limitation of inferring flow distribution from sampled traffic.
    A data-streaming algorithm was proposed in Kumar et al. (2004a) for providing very accurate esti-
mates of flow-size distribution. The algorithm uses a very simple lossy data structure: a large array of
passive counters. Upon the arrival of a packet at the router, its flow label is hashed to generate an index
into this array, and the counter at this index is incremented by 1. Collisions due to hashing might cause
two or more flow labels to be hashed to the same indices. Counters at such an index would contain
the total number of packets belonging to all of the flows colliding into this index. There is no explicit
mechanism to handle collisions because any such mechanism would impose additional processing and
storage overheads that are unsustainable at high speeds.
    The online streaming process is simple: Each packet arrival results in only a hashing operation and
a counter increment. This streamlined (pun intended) design allows the online streaming process to
operate at speeds as high as OC-768 without missing any packets. Furthermore, since during the online
streaming phase the counters only need to be incremented (by 1), it suffices to use an array of passive
counters. Such a counter array can be very cost-effectively implemented using a DRAM backing-store
scheme such as RS (Zhao et al., 2006b) (described in Section 16.3).
    The data structure is lossy in the sense that, due to collision in hashing, sizes of multiple flows may
be accumulated in the same counter. Therefore, the raw information obtained from the counters can
be far away from the actual flow distribution. This algorithm then uses Bayesian statistical methods
such as expectation–maximization (EM) to infer the most likely flow-size distribution that results in the
observed counter values after collision.
    For achieving high accuracy, the number of counters used needs to be on the same order as the
number of active flows O(N ) in a measurement epoch. Hence, its space requirement is linear with
respect to N rather than sublinear as desired. However, since the constant factor is very small, this cost
is still modest even for very high-speed links and is justifiable since the flow-size distribution subsumes
and contains much more information than other statistics of traffic. Indeed, we will show in the next
few sections that, when the objective is a simple function of this distribution, the space requirement can
become much smaller.

16.19 The Tug-of-War algorithm for estimating F2                 485
