# network-algorithmics-16-7-reducing-counters-using-threshold-aggregation (chunk 000003)

There are at most 99,900/900 = 111 such buckets out of the 1000 at each stage. Therefore, the prob-
ability of passing one stage is at most 11.1%. With four independent stages, the probability that a small
flow no larger than 100 KB passes all four stages is the product of the individual stage probabilities,
which is at most 1.52 ∗ 10−4 .
     Note the potential scalability of the scheme. If the number of flows increases to one million, we
simply add a fifth hash stage to get the same effect. Thus, to handle 100,000 flows requires roughly
4000 counters and a flow memory of approximately 100 memory locations; to handle one million flows
requires roughly 5000 counters and the same size of flow memory. This is logarithmic scaling.
     The number of memory accesses at packet arrival time performed by the filter is exactly one read
and one write per stage. If the number of stages is small enough, this is affordable, even at high speeds,
since the memory accesses can be performed in parallel, especially in chip implementation. A simple
optimization called conservative update (see the exercises) can improve the performance of multistage
filtering even further. Multistage filters can be seen as an application of Principle P3a, trading certainty
(allowing some false positives and false negatives) for time and storage.
