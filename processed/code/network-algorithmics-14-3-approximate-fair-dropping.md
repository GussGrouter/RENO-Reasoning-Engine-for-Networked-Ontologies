# Network Algorithmics — 14.3 Approximate fair dropping (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 416
- Slice: from `14.3 Approximate fair dropping` up to next detected section heading

---

14.3 Approximate fair dropping
One may rightly argue that RED is an admission-control rather than a packet scheduling algorithm, in
that the router simply transmits all packets admitted by (i.e., not dropped by) RED in the FIFO order.
Later in this chapter, we will focus on real packet scheduling algorithms that decide on an appropriate
transmission order among packets belonging to multiple competing classes or flows, that leads to a fair
bandwidth allocation. Compared to these real packet scheduling algorithms, RED and its variants (e.g.,
weighted RED currently used by Cisco routers) incur less computational and system overheads, but do
a worse job of fair bandwidth allocation among competing flows. There is really nothing wrong with
this tradeoff: RED and its variants were originally designed for congestion control only, and that it can
achieve some degree of fair bandwidth allocation is arguably already a bonus. Hence, it was a pleasant
surprise when a technique called approximate fair dropping (AFD) (Pan et al., 2008) was proposed
that has similar computational and system overheads as RED, yet provides a level of fair bandwidth
allocation that is comparable to some such real packet scheduling algorithms, such as Deficit Round
Robin (DRR) that we will describe in Section 14.7.2.
    As explained earlier, weighted RED also performs differential dropping per traffic class (or flow).
However, weighted RED cannot be configured to induce a target allocation of the link bandwidth (say
according to a certain fairness criteria) accurately, as shown in Pan et al. (2008). In comparison, AFD
provides a level of bandwidth allocation that is almost as fine-grained and accurate as DRR, as also
shown in Pan et al. (2008). The key idea of AFD is very simple. The time is divided into epochs that
are a few RTTs in length. The router measures and estimates the traffic arrival rate of each class during
the current epoch, for the purpose of setting the dropping rate for each class during the next epoch.

390      Chapter 14 Scheduling packets



Suppose the estimated arrival rate of class i is ri during the current epoch. Then, during the next epoch,
the dropping rate Di for class i traffic is set in such a way that the discounted (by dropping) arrival rate
                                   f           f
ri (1 − Di ) is equal to min(ri , ri ), where ri is the fair sending rate allocated to flow i. The fair sending
         f
rates (ri )’s for all traffic classes are determined by the (estimated) arrival rates of all classes and the
link bandwidth r, using the max-min fairness criteria.
     It was shown in Pan et al. (2008) that AFD can induce any target bandwidth allocation almost as
accurately as DRR. To this end, AFD incurs less systems overheads than DRR: AFD does not require
extra packet buffers whereas DRR requires packets to be demultiplexed into and buffered at per-class
or per-flow queues, as we will explain in Section 14.7.2; and both AFD and DRR incur the same O(1)
computational complexity for processing an incoming packet. Hence, overall AFD offers a bigger bang
for the buck than DRR. Both DRR and AFD are currently used in Cisco switch and router products.
