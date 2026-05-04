# network-algorithmics-14-14-1-fair-round-robin-frr-algorithm (chunk 000002)

is O(log G)), since in this (FRR’s) use case (of WF2 Q) the weight of a group can change dynamically
(say when a constituent flow of a group becomes newly backlogged) whereas in a standard use case, the
weight of a flow never changes; however, since G is small (G ≤ 64 as explained above), O(G log G)
is technically still O(1). Note such fine-grained scheduling among groups (using this WF2 Q variant)
is necessary for FRR to achieve good fairness, since (the constituent flows of) different super flows
can have very different weights, and using a coarse-grained scheduler among them can result in a poor
T-WFI that grows linearly with n as explained above.
    Once FRR picks a group for service, it picks the HOL packet of one of the flows belonging to the
group for service according to a round-robin order using an extended form of DRR; note even a round-
robin scheduler can achieve good fairness when scheduling flows within a group, since these flows have
similar weights by design. Using this two-tiered approach, FRR achieves excellent overall fairness yet
has a low time complexity that is technically O(1).
