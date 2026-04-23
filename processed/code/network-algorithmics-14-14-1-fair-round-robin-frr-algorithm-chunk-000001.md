# network-algorithmics-14-14-1-fair-round-robin-frr-algorithm (chunk 000001)

# Network Algorithmics — 14.14.1 Fair round robin (FRR) algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 446
- Slice: from `14.14.1 Fair round robin (FRR) algorithm` up to next detected section heading

---

14.14.1 Fair round robin (FRR) algorithm
To be fair, QFQ is not the first scheduling algorithm to be nearly as fair as WF2 Q yet have O(1) time
complexity. Fair Round Robin (FRR) (Yuan et al., 2009) is the first such algorithm. In the following,
we describe FRR first, since QFQ builds and improves on FRR. The design of FRR is based on the
following insight: It is computationally much easier to schedule n flows with equal or similar weights
than that with very different weights (that can differ from one another by O(n) times such as that in
the example shown in Fig. 14.18). This insight can be seen from the following two facts: (1) When all
flows have the same weight or similar weights, the T-WFI of even a round robin scheduler (that has
O(1) time complexity) such as DRR does not grow with n; (2) when flows have very different weights
however, the T-WFI of even the WFQ (that has O(log n) time complexity) grows linearly with n as
shown in Section 14.11.
    Based on this insight, the idea of FRR is to bundle flows into groups such that in each group,
the weights of flows are similar. The grouping is done in the following “exponential” manner: Each
flow Fk belongs to the group i = logC φk , where φk is the weight of Fk . Here C is a parameter that
controls the tradeoff between the time complexity of FRR and the service guarantees FRR provides;
larger C leads to fewer number of groups and hence better time complexity, but also to worse QoS
guarantees (more specifically worse delay bounds). C is typically set to an integer value such as 2. For
convenience of presentation, we assume C = 2 in the sequel. In this case, in each group, weights of
flows can differ by at most 2 times. One effect of this grouping is that the number of groups, which we
denote as G, is independent of n, or in other words is O(1) with respect to n. It is not hard to show that
G = logC (φmax /φmin ) where φmax and φmin are the maximum and the minimum weight of a flow,
respectively. When C = 2, we have G ≤ 64 under all conceivably use cases.
    After bundling flows into groups, FRR takes the following two-tiered approach towards cost-
effective packet scheduling: It performs fine-grained scheduling among groups and coarse-grained
scheduling among flows within a group (P3b) as follows. FRR views each group (of flows) as a super
flow, and serves these G super flows using a variant of WF2 Q. This variant, which has a time complex-
ity of O(G log G), is more computationally expensive than the vanilla WF2 Q (whose time complexity

420      Chapter 14 Scheduling packets
