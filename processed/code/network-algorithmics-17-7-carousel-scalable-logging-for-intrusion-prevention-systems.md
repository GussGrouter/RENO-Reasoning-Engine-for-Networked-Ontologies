# Network Algorithmics — 17.7 Carousel: scalable logging for intrusion prevention systems (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 535
- Slice: from `17.7 Carousel: scalable logging for intrusion prevention systems` up to next detected section heading

---

17.7 Carousel: scalable logging for intrusion prevention systems
In this section we first describe a network security problem that looks trivial but is in fact challeng-
ing because naive solutions can deliver poor performance. We then present a simple solution called
Carousel (The Lam et al., 2010) that leverages hashing and sampling in an unusual way.

                   17.7 Carousel: scalable logging for intrusion prevention systems                    509



     Consider an application scenario in which an enterprise network containing a large number of hosts
is monitored and protected by an intrusion prevention system (IPS). We assume that the IPS, which, by
sitting in a strategic position, can “see” all the packets transiting in the network. When a widespread
security event happens to this network, the IPS is tasked with logging, to its disk or SSD (solid state
drive), every distinct IP address involved in this event and a succinct event report associated with the
IP address.
     One such security event is the infection of many of its hosts by a worm. In this event for each IP
address (host) already infected by the worm, the IPS needs to record it along with a packet sent from the
host that serves as the evidence (event report). Here for simplicity, we assume that, upon examining the
header and the content of a packet, IPS can decide whether the packet is “infectious”; if so, its source
IP address needs to be logged. Our goal in this application scenario is to design a scalable solution for
the IPS to log all these IP addresses and their associated event reports.
     For ease of presentation, in the rest of this section we use this application scenario (of assessing the
scale of a worm attack) as the context for formulating our problem. Before we can get to the gist of this
problem, however, we need to make two additional assumptions. First, we assume that each infected
source (IP address) sends out a large number of packets (trying to infect others).
     With this assumption, the naive solution of logging the source (or destination) IP address of every
“infectious” packet does not work well, since it can log an infected source many times, which can lead
to poor throughput performance, as we will elaborate shortly. In other words, a good solution needs to
somehow filter out most of the duplicates and ideally log each infected source only once.
     Second, we assume that each infected source is persistent in the sense that it will send out “infec-
tious” packets for a relatively long period of time. This is really an “enabling” assumption in the sense
that without the assumption, it appears hard, if not impossible, to design an elegant solution to our
problem, as we will explain shortly. On the other hand, this assumption is also reasonable for this appli-
cation for the following reason. The very purpose for logging infected sourcess is to “neutralize” and if
possible remediate such sources. If an infected source has stopped sending packets, it no longer poses
a clear and present danger as far as the spreading of this particular (suspected) worm is concerned. In
this case, to log its IP address is less important than logging those persisent sources (worm spreaders).
     We now make our first attempt at formulating the problem using the data streaming language we
have introduced in Section 16.15. Consider a stream of data items, each of which is the source IP
address of an infectious packet, that arrive at the IPS at a very high rate. With high probability, each
such IP address appears many times (the first additional assumption above) and does so persistently (the
second additional assumption above) in the stream. Our problem is for the IPS to gather a near-complete
list of such IP addresses after performing one-pass processing of the data stream. This problem is
intuitively more difficult than the problem of counting the number of distinct elements (explained in
Section 16.16): here we need to write down the list of distinct elements.
     Like many other network algorithmics problems, this problem would be trivial if we did not have
stringent performance expectations for an ideal solution. In this case our expectations, to be stated next,
are reasonable with respect to the resource constraints of the system.
     Suppose the total number of such IP addresses is a large number N and the bandwidth of the disk
in the IPS is b. Suppose the IPS has certain resource constraints (which we will elaborate shortly)
that prevent various clever “smoothing” or “work amortization” tricks (e.g., via caching or buffering in
memory) from being used to speed up this logging task. Then intuitively an ideal solution can attain
no more than a maximum “throughput” of b, so it would need at least N/b amount of time to log the

510      Chapter 17 Network security



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

                                                                              17.9 Exercises         511
