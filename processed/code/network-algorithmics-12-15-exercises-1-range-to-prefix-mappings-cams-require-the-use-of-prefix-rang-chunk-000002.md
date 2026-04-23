# network-algorithmics-12-15-exercises-1-range-to-prefix-mappings-cams-require-the-use-of-prefix-rang (chunk 000002)

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
