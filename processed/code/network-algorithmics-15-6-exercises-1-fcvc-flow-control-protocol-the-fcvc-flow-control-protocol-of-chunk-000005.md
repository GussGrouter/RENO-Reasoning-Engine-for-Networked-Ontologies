# network-algorithmics-15-6-exercises-1-fcvc-flow-control-protocol-the-fcvc-flow-control-protocol-of (chunk 000005)

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
