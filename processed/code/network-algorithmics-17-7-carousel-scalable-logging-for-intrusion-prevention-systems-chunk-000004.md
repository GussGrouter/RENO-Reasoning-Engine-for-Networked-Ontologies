# network-algorithmics-17-7-carousel-scalable-logging-for-intrusion-prevention-systems (chunk 000004)

vast majority of these N identities (at least once). Our problem is to come up with such an ideal solu-
tion. Clearly, the aforementioned naive solution of logging the IP addresses of all “infectious” packets
without any duplicate filtering has a much poorer throughput performance than the ideal solution, since
many IP addresses can each appear in a large number of packets.
     We start by explaining the aforementioned “anti-smoothing” resource constraint and why another
naive solution does not work under it. A typical, and perhaps expected (by readers who have gone this
far in reading this book) constraint is that the amount of memory (say M) that the IPS has available
for this logging task is much smaller than that is needed to store all N identifies. This is a reasonable
constraint since, for the IPS to scan each and every packet in the network in real-time, this memory has
to be SRAM.
     Under this constraint, the naive solution of filtering out duplicates via keeping a hash table of all
“infectious” IP addresses seen and logged so far does not work because the hash table clearly cannot
fit in the memory (SRAM). Although using a Bloom filter instead reduces the memory footprint by
roughly an order of magnitude (at the cost of some false positives as explained in Section 17.4.1),
the Bloom filter may still be too large to fit in the memory. We call this constraint “anti-smoothing”
because without this constraint, IPS can simply gather all distinct IP addresses (and filter out duplicates)
in memory and write them to disk at the ideal throughput of b.
     Now we are ready to describe Carousel (The Lam et al., 2010), which solves the problem of logging
most of the distinct elements while filtering out most of the duplicates. The solution is in fact quite
simple. Its basic idea is first divide the IP address space statistically evenly into K subspaces (partitions)
so that roughly N/K distinct “infectious” IP addresses fall into each partition.
     Then Carousal takes turns (“rotates around”) to perform this logging task for each and every par-
tition, one at a time; this rotation gives the scheme its name. When focusing on a partition, Carousal
processes each packet whose source IP address falls into the partition using a Bloom filter (to filter out
duplicates) and logs most of the roughly N/K distinct elements in this partition. The parameter K is set
to be just large enough for the Bloom filter encoding these N/K distinct elements to fit in the amount
of memory M available for this logging task.
     Once the Bloom filter is close to full (when roughly half or more of its bits are set to 1), the IPS
writes these IP addresses to the disk and moves on to the next partition. Such a partitioning can be
easily achieved via hashing. It was shown in The Lam et al. (2010) that, when the disk throughput b
is the performance bottleneck, Carousel can accomplish this logging mission in roughly N/b seconds,
assuming that Carousel commits the list of distinct IP addresses found in the current partition to the
disk at the same time as it processes the next partition (using a Bloom filter) in memory.
     Note that the assumption made earlier that nearly every such IP address appears persistently (i.e.,
for a “long enough” period of time) is necessary because it takes Carousel roughly N/b seconds to
“rotate around” and “visit” every partition.
     The last remaining issue is how to pick the right value for K, the number of partitions. Making K
too large leads to an unnecessarily long delay for logging all distinct elements. Making K too small
overcrowds the Bloom filter and leads to high false positives, which would result in many IP addresses
being misclassified as duplicates and not being logged. A typical solution is an adaptive one: to start
with a conservative (larger) K, which is typically a power of 2, and adjust it by halving it when the
Bloom filter is found to be underpopulated (when much less than half of its bits have value 1).
