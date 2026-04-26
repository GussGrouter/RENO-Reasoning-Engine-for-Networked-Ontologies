# Network Algorithmics — 15.6 Exercises 1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 471
- Slice: from `15.6 Exercises 1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides` up to next detected section heading

---

15.6 Exercises
1. FCVC flow control protocol: The FCVC flow control protocol of Kung et al. (1994) provides
   an important alternative to the credit protocols described in Section 15.1. In the FCVC protocol,
   shown in Fig. 15.5, the sender keeps a count of cells sent H , while the receiver keeps a count
   of cells received R and cells dequeued D. The receiver periodically sends its current value of D,
   which is stored at the sender as estimate L. The sender is allowed to send if H − L > Max. More
   importantly, if the sender periodically sends H to the receiver, the receiver can deal with errors due
   to cell loss.

   • Assume cells are lost and that the sender periodically sends H to the receiver. How can the
     receiver use the values of H and R to detect how many cells have been lost?
   • How can the receiver use this estimate of cell loss to fix D and so correct the sender?

                                                                                      15.6 Exercises           445




FIGURE 15.5
The FCVC protocol uses a count H of cells sent by the sender and an estimated L of the cells dequeued at the re-
ceiver; flow control is achieved by limiting the difference between H and L. More importantly, the use of absolute
packet numbers instead of incremental credits allows the periodic sending of counts to fix errors due to cell loss.


   • Can this protocol be made self-stabilizing without using the full machinery of a snapshot and
     reset?
   • Compare the general features of this method of achieving reliability to the method used in the
     load-balancing algorithm described in the chapter.

2. Load balancing with variable-sized packets: Load balancing within a router is typically at the
   granularity of cells. However, load balancing across routers is often at the granularity of (variable-
   sized) packets. Thus simple round-robin striping may not balance load equally because all the large
   packets may be sent on one link and the small ones on another. Modify the load-balancing algorithm
   without sequence numbers (using ideas suggested by the deficit round-robin (DRR) algorithm de-
   scribed in Chapter 14) to balance the load evenly, even while striping variable-sized packets. Extend
   the fault-tolerance machinery to also handle this case.
3. Concurrent compaction and search: In many lookup applications, routers must use available on-
   chip SRAM efficiently and may have to compact memory periodically to avoid filling up memory
   with unusably small amounts of free space. Imagine a sequence of N trie nodes of size-4 words
   that are laid out contiguously in SRAM memory, after which there is a hole of size-2 words. As
   a fundamental operation in compaction, the update algorithm needs to move the sequence of N
   nodes two words to the right to fill the hole. Unfortunately, moving a node two steps to the right can
   overwrite itself and its neighbor. Find a technique for doing compaction for updating with minimal
   disruption to a concurrent search process. Assume that, when a node X is moved, there is at most one
   other node Y that points to X and that the update process has a fast technique for finding Y given X
   (see Chapter 11). Use this method to find a way to compact a sequence of trie nodes arbitrarily laid
   out in memory into a configuration where all the free space is at one end of memory and there are
   no “holes” between nodes. Of course, the catch is that the algorithm should work without locking
   out a concurrent search process for more than one write operation every K search operations, as in
   the bridge binary search example.

This page intentionally left blank

                                                                                       PART

Endgame
                                                                                    4
              Daring ideas are like chessmen moved forward. They may be beaten, but they may start a winning
                                                                                                       game.
                                                                                                   —Goethe

                                                             We didn’t lose the game; we just ran out of time.
                                                                                           —Vince Lombardi


The last part of the book applies network algorithmics to the emerging fields of security and measure-
ment. As the Internet matures, we believe that good abstractions for security and measurement will be
key to well-engineered networks. While the problems (e.g., detecting a denial-of-service (DoS) attack at
a high-speed router) seem hard, some remarkable ideas have been proposed. The final chapter reaches
closure by distilling the underlying unities behind the many different techniques surveyed in this book
and by surveying the future of network algorithmics.

This page intentionally left blank

                                                                                                           CHAPTER


Measuring network traffic
                                                                                                   16
                                      Not everything that is counted counts, and not everything that counts can be counted.
                                                                                                          —Albert Einstein


Every graduate with a business degree knows that the task of optimizing an organization or process
begins with measurement. Once the bottlenecks in a supply chain are identified and the major cost
factors are outlined, improvements can be targeted. The situation is no different in computer networks.
For example, in service provider networks packet counting and logging provide powerful tools for the
following.
Capacity Planning: Internet service providers (ISPs) need to determine the traffic matrix or the traffic
     between all source and destination subnets they connect. This knowledge can be used on short time
     scales (say, hours) to perform traffic engineering by reconfiguring optical switches; it can also be
     used on longer time scales (say, months) to upgrade link capacity.
Accounting: Internet service providers implement complex service-level agreements (SLAs) with
     customers and peers. Simple accounting arrangements based on overall traffic can easily be mon-
     itored by a single counter; however, more sophisticated agreements based on traffic type require a
     counter per traffic type. Packet counters can also be used to decide peering relationships. Suppose
     ISP A is currently sending packets to ISP C via ISP B and is considering directly connecting (peer-
     ing) with B; a rational way for A to decide is to count the traffic destined to prefixes corresponding
     to B.
Traffic Analysis: Many network managers monitor the relative ratio of one packet type to another. For
     example, a spike in peer-to-peer traffic may require rate limiting. A spike in ICMP messages may
     indicate a Smurf attack.
    Once causes—such as links that are unstable or have excessive traffic—are identified, network op-
erators can take action by a variety of means. Thus measurement is crucial not just to characterize the
network but to better engineer its behavior.
    There are several control mechanisms that network operators currently have at their disposal. For
example, operators can tweak Open Shortest Path First (OSPF) link weights and BGP policy to spread
the load, can set up circuit-switched paths to avoid hot spots, and can simply buy new equipment. This
chapter focuses only on network changes that address the measurement problem—i.e., changes that
make a network more observable. However, we recognize that making a network more controllable,
for instance, by adding more tuning knobs, is an equally important problem we do not address here.
    Despite its importance, traffic measurement, at first glance, does not appear to offer any great
challenges or have much intellectual appeal. As with mopping a floor or washing dishes, traffic mea-
surement appears to be a necessary but mundane chore.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00024-5
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                     449

450      Chapter 16 Measuring network traffic



    The goal of this chapter is to argue the contrary: that measurement at high speeds is difficult because
of resource limitations and lack of built-in support; that the problems will only grow worse as ISPs
abandon their current generation of links for even faster ones; and that algorithmics can provide exciting
alternatives to the measurement quandary by focusing on how measurements will ultimately be used.
To develop this theme, it is worth understanding right away why the general problem of measurement
is hard and why even the specific problem of packet counting can be difficult.
    This chapter is organized as follows. Section 16.1 describes the challenges involved in measurement.
Section 16.2 shows how to reduce the required width of an SRAM counter using a DRAM backing-
store and introduces two different schemes, both of which are deterministic algorithms, for that purpose.
Section 16.3 describes a randomized algorithm for the same purpose that is much simpler and much
more SRAM-efficient. These three counter schemes all implement passive counters, in which counters
need to handle increments, but not read accesses, in real time.
    Section 16.4 describes an SRAM-efficient scheme called BRICK for maintaining active counters
that need to handle both in real time. In network measurement applications each counter is associated
with a traffic flow, and the value of the counter is a special and very simple type of state information
associated with the flow. Section 16.5 describes an extension of BRICK for efficiently maintaining
general state information for many traffic flows.
    Section 16.6 details a different technique for reducing counter widths by using randomized counting,
which trades accuracy for counter width. Section 16.7 presents a different approach to reducing the
number of counters required (as opposed to the width) by keeping track of counters only above a
threshold. Section 16.8 shows how to reduce the number of counters even further for some applications
by counting only the number of distinct flows.
    Techniques in prior sections require computation on every packet. Section 16.9 takes a different
tack by describing the sampled NetFlow technique for reducing packet processing; in NetFlow only a
random subset of packets is processed to produce either a log or an aggregated set of counters. Sec-
tion 16.10 shows how to reduce the overhead of shipping NetFlow records to managers. Section 16.11
explains how to replace the independent sampling method of NetFlow with a consistent sampling tech-
nique in all routers that allow packet trajectories to be traced.
    The next three sections of the chapter move to a higher-level view of measurement. In Section 16.12
we describe a solution to the accounting problem. This problem is of great interest to ISPs, and the
solution method is in the best tradition of the systems approach advocated throughout this book. In
Section 16.13 we describe a solution to the traffic matrix problem using the same concerted systems
approach. Section 16.14 presents a very different approach to measurement, called passive measure-
ment, that treats the network as a black box. It includes an example of the use of passive measurement
to compute the loss rate to a Web server.
    The last six sections of this chapter provide a small sample of a fascinating new algorithmic tool
to network measurement that has been developed mostly in the new millennium: data streaming and
sketching algorithms (Muthukrishnan, 2005). These algorithms can, among other things, generate more
informative and hence better traffic logs for a variety of measurement tasks. Section 16.15 provides a
brief introduction to the data streaming model and the design objectives of data streaming algorithms.
Section 16.16 revisits the counting of the number of distinct flows from a new data-streaming perspec-
tive. One such data-streaming algorithm, called min-hash sketch, leads to an unexpected solution to a
classical database problem called associative-rule mining.

                                                                   16.1 Why measurement is hard                        451



    With this new perspective Section 16.17 revisits the elephant or heavy-hitter detection problem
introduced in Section 16.7. Section 16.18 describes a data-streaming algorithm for estimating the dis-
tribution of flow sizes in a high-speed link. Finally, Section 16.19 describes the celebrated Tug-of-War
(ToW) algorithm for estimating the second moment of a data stream. This algorithm was introduced in
a seminal paper on data streaming, for which the authors, Noga Alon, Phillip Gibbons, Yossi Matias,
and Mario Szegedy, received the 2019 ACM Paris Kanellakis Theory and Practice Award.
    The implementation techniques for the measurement primitives described in this chapter (and the
corresponding principles used) are summarized in Table 16.1.

  Quick reference guide
  Section 16.2 may be of interest to a network device implementor seeking to implement a large number of counters at
  high speeds. Section 16.3 describes a hybrid SRAM/DRAM scheme for efficiently maintaining a large number of passive
  counters that has been used in Huawei router products since 2010. Section 16.4 describes an SRAM-efficient scheme for
  maintaining a large number of active counters. Section 16.5 describes an extension of BRICK for efficiently maintaining
  general state information for many traffic flows. Section 16.8 describes a useful mechanism for quickly counting the
  list of distinct identifiers in a stream of received packets without keeping large hash tables. Section 16.12 presents a
  solution proposed by Juniper Networks for accounting. Section 16.13 covers inferring traffic matrices and is useful for
  implementors building tools for monitoring ISPs.




              Table 16.1 Principles used in the implementation of the measurement
              primitives discussed in this chapter.
              Number                     Principle                                         Used in
                P5c  Low-order counter bits in SRAM, all bits in DRAM                  LCF algorithm
               P15         Update only counters above threshold                         LR algorithm
               P3b                 Randomized counting                                Morris algorithm
                P3a    Multiple hashed counters to detect heavy flows                 Multistage filters
               P3b       Flow counting by hashing flows to bitmaps                  Multiresolution bitmap
                P3a    Packet sampling to collect representative logs                Sampled NetFlow
                P3a         Sampling flows proportional to size                      Sampled charging
                P3           Aggregating prefixes into buckets
                                                                                        Juniper’s DCU
                P4          Routing protocol helps color prefixes
                P4         Using TCP semantics for measurement                              Sting
                P3a   Allow counter updates to be missed occasionally                    RS algorithm
                P7         Optimize for a restricted access pattern
                                                                                            BRICK
                P4c               Use built-in instructions
