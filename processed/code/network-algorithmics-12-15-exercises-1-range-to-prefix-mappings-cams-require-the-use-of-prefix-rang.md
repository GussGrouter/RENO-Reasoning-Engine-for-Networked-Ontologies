# Network Algorithmics — 12.15 Exercises 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 355
- Slice: from `12.15 Exercises 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general` up to next detected section heading

---

12.15 Exercises
 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general
    ranges. Describe an algorithm that converts an arbitrary range on, say, 16-bit port number fields
    to a logarithmic number of prefix ranges. Describe the prefix ranges produced by the arbitrary but
    common range of greater than 1024. Given a rule R with arbitrary range specifications on port
    numbers, what is the worst-case number of CAM entries required to represent R? Solutions to this
    problem are discussed in Srinivasan et al. (1998, 1999).
 2. Worst-Case Storage for Set-Pruning Tries: Generalize the example of Fig. 12.5 to K fields to
    show that storage in set-pruning-trie approaches can be as bad as O(N k /k).
 3. Improvements to the Grid of Tries: In the grid of tries, the only role played by the destination trie
    is in determining the longest-matching destination prefix. Show how to use other lookup techniques
    to obtain a total search time of (log W + W ) for the destination–source rules instead of 2W .
 4. Reasoning about the Correctness of the Grid of Tries: Given any source and destination IP
    address pair (o, d), let S be the set of nodes (destination-source rules) that (o, d) matches with. A

                                                                             12.15 Exercises          329



    node α in S is called a skyline point if there is no other node (rule) in S whose source and destina-
    tion prefixes are both no shorter than those of node α. Now solve the following two subproblems.
    First, prove that the grid of tries algorithm guarantees to traverse all skyline points in S. Second,
    explain why this guarantee, in combination with the pre-computation of the stored rule for each
    node, is sufficient to guarantee the correctness of the grid of tries algorithm.
 5. Aggregate Bit Vector Search: Use 3-bit summaries in Fig. 12.11 and determine the improvement
    in the worst-case time by adding summaries, and compare it to the increase in storage for using
    summaries. Details of the algorithm, if needed, can be found in Baboescu and Varghese (2001).
 6. Aggregate Bit Vector Storage: The use of summary bits appears to increase storage. Show, how-
    ever, a simple modification in which the use of aggregates can reduce storage if the bit vectors
    contain large strings of zeroes. Describe the modifications to the search process to achieve this
    compression. Does it slow down search?
 7. On-Demand Cross-Producting: Consider the database of Fig. 12.2, and imagine a series of Web
    accesses from an internal site to the external network. Suppose the external destinations accessed
    are D1 , . . . , DM . How many cache terms will these headers produce in the case of full header
    caching versus on-demand cross-producting?
 8. Equivalenced Cross-Producting: Why do the fifth and eighth entries in Fig. 12.13 have the same
    bitmaps? Check your answer two ways, first by intersecting the corresponding bitmaps for the two
    fields from Fig. 12.11 and then by arguing directly that they match the same set of rules.
 9. Combining Trees for RFC: The equivalenced cross-producting idea in RFC leaves unspecified
    how to choose a combining tree. One technique is to compute all possible combining trees and then
    to pick the tree with the smallest storage. Describe an algorithm based on dynamic programming
    to find the optimal tree. Compare the running times of the two algorithms.
10. Reducing Rule Databases Using Redundancy: If a smaller prefix has the same next hop as a
    longer prefix, the longer prefix can be removed from an IP lookup table. Find similar techniques
    to spot redundancies in classifiers. Compare your ideas with the techniques described in Gupta
    and McKeown (1999a). Note that as in the case of IP lookups, such techniques to remove redun-
    dancy are orthogonal to the classification scheme chosen and can be implemented in a separate
    preprocessing step.
11. Generalizing Linear Searching in HiCuts: In HiCuts, all the linear lists are at the leaves. How-
    ever, a rule with all wildcarded entries will be replicated at all leaves. This suggests that such rules
    be placed once in a linear list at the root of the HiCuts tree. Generalizing, one could place linear
    lists at any node to reduce storage. Describe a bottom-up algorithm that starts with the base HiCuts
    decision tree and then hoists rules to nodes higher up in the tree to reduce storage. Try to do so
    with minimal impact on the search time.

This page intentionally left blank

                                                                                                        CHAPTER


Switching
                                                                                                 13
                                                                                           I’d rather fight than switch.
                                                                           —Tareyton Cigarettes ad, quoted by Bartlett’s


In the early years of telephones the telephone operator helped knit together the social fabric of a com-
munity. If John wanted to talk to Martha, John would call the operator and ask for Martha; the operator
would then manually plug a wire into a patch panel that connected John’s telephone to Martha’s. The
switchboard, of course, allowed parallel connections between disjoint pairs. James could talk to Mary
at the same time that John and Martha conversed. However, each new call could be delayed for a brief
period while the operator finished putting through the previous call.
    When transistors were invented at Bell Labs, the fact that each transistor was basically a voltage-
controlled switch was immediately exploited to manufacture all-electronic telephone switches using an
array of transistors. The telephone operator was then relegated to functions that required human inter-
vention, such as making collect calls. The use of electronics greatly increased the speed and reliability
of telephone switches.
    A router is basically an automated post office for packets. Recall that we are using the word router
in a generic sense to refer to a general interconnection device, such as a gateway or a SAN switch.
Returning to the familiar model of a router in Fig. 13.1, recall that in essence a router is a box that
switches packets from input links to output links. The lookup process (B1 in Fig. 13.1) that determines
which output link a packet will be switched to was described in Chapter 11. The packet scheduling
done at the outbound link (B3 in Fig. 13.1) is described in Chapter 14. However, the guts of a router
remain its internal switching system (B2 in Fig. 13.1), which is discussed in this chapter.
    This chapter is organized as follows. Section 13.1 compares router switches to telephone switches.
Section 13.2 details the simplicity and limitations of a shared memory switch. Section 13.3 describes
router evolution, from shared buses to crossbars. Section 13.4 presents a simple matching algorithm
for a crossbar scheduler that was used in DEC’s first GigaSwitch product. Section 13.5 describes a
fundamental problem with DEC’s first GigaSwitch and other input-queued switches, called head-of-
line (HOL) blocking, which occurs when packets waiting for a busy output delay packets waiting for
idle outputs. Section 13.6 covers the knockout switch, which avoids HOL blocking, at the cost of some
complexity, by queuing packets at the output.
    Section 13.7 introduces the now standard solution approach to HOL blocking called virtual output
queueing (VOQ). The VOQ approach however leads to the problem of computing bipartite matchings,
introduced in Section 13.8, which is much more sophisticated and challenging than that in the case
of GigaSwitch. Section 13.9 presents the first such bipartite matching algorithm called PIM. PIM is a
randomized algorithm that retains the simplicity of input queuing; this scheme was deployed in DEC’s
second GigaSwitch product. Section 13.10 describes iSLIP, a scheme that appears to emulate PIM, but
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00020-8
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                  331

332      Chapter 13 Switching




FIGURE 13.1
Router model.


without the use of randomization. iSLIP is found in a number of router products, including the Cisco
GSR.
     Neither PIM nor its derandomized version iSLIP can achieve close to 100% throughput under all
traffic patterns. In addition, if implemented as a centralized algorithm, both PIM and its derandomized
version iSLIP have a fairly high time complexity of O(N log2 N ), where N is the number of input
and output ports. Section 13.11 introduces an incremental learning-based approach to computing bipar-
tite matchings, which is taken by the four algorithms we describe next: sample-and-compare SERENA,
QPS, and Sliding-Window QPS (SW-QPS). Section 13.12 describes an extremely simple centralized al-
gorithm, called sample-and-compare, that can provably achieve 100% throughput and has a lower time
complexity of O(N ). Its delay performance under heavy loads, however, is poor. Section 13.13 de-
scribes an improved algorithm called SERENA that, like sample-and-compare, also can achieve 100%
throughput and has O(N ) time complexity, but has much better delay performance under heavy loads
than sample-and-compare. SERENA is only a slight modification of sample-and-compare that replaces
the “compare” operation with a “merge” operation. Section 13.14 introduces a new sampling strategy
called queue-proportional sampling (QPS), that, if used to replace the “sample” operation in SERENA
or to generate a starter matching for iSLIP, can further improve their delay performances. Using QPS,
an input port can, in O(1) time, sample and propose to match with an output port, with a probability
that is proportional to the number of packets (currently in the queue of the input port) destined for that
output port. The data structure that enables this O(1) time complexity is described in Section 13.15.
The pursuit for better monolithic bipartite matching algorithms culminates in a late-breaking paral-
lel iterative algorithm called sliding-window QPS (SW-QPS), to be described in Section 13.16, that
achieves overall better throughput and delay performances than iLSIP, yet has only a O(1) time com-
plexity per input or output port. Finally, in Section 13.17, we describe the Combined Input and Output
Queueing (CIOQ) proposal that advocates combining switching with packet scheduling for providing
QoS guarantees.
     As various hurdles exist for existing monolithic switching schemes to scale to a large number of
ports, Section 13.18 describes two approaches to that end. Each achieves the scalability objective by
reducing a different switching cost. One reduces the overall size of the switch circuitry through the

                                                        13.1 Router versus telephone switches                          333



use of more space-efficient switch fabrics than a monolithic crossbar, such as the Clos and the Benes
fabrics. The other, called load-balanced switching (LBS), reduces the algorithmic cost of matching
computation to virtually zero, as it requires no such computation at all. However, it does so by using
two crossbars instead of one.
    Section 13.19 shows how to scale switches to faster link speeds by using bit-slice parallelism and
by using shorter fabric links as implemented in the Avici TSR.
    The literature on switching is vast, and this chapter can hardly claim to be representative. In the
first edition, this section mostly covers switch designs that had been built, analyzed in the literature,
and actually used in the networking industry. They include DEC’s GigaSwitch, Cisco’s GSR, Juniper’s
T-series, and Avici’s TSR. In this edition, we have added several new switching schemes that emerged
after the early 2000s, such as SERENA, QPS, SW-QPS, and the LBS algorithms. With these updates,
we believe this section now strikes a better balance between the practical and the theoretical issues that
arise in designing switch fabrics for high-speed routers.
    The switching techniques described in this chapter (and the corresponding principles invoked) are
summarized in Table 13.1.

  Quick reference guide
  Many of the switching algorithms described in this chapter have actually been built. However, for an implementor doing
  a quick first reading, we suggest first reviewing the iSLIP algorithm, which is implemented in the Cisco GSR (Sec-
  tion 13.10). While iSLIP works very well for moderate-sized switch fabrics, Section 13.18 describes solutions that scale
  to large switches, including the Clos fabric used by Juniper Networks. Sections 13.14 through 13.16 describe a mind-
  blowing new technology, called Queue-Propotional Sampling (QPS) and Sliding-Window QPS (SW-QPS), that will make
  us rethink how switching should be implemented in the future.
