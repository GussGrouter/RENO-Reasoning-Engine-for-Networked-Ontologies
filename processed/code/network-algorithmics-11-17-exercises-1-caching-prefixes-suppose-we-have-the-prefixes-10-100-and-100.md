# Network Algorithmics — 11.17 Exercises 1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 318
- Slice: from `11.17 Exercises 1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like` up to next detected section heading

---

11.17 Exercises
1. Caching Prefixes: Suppose we have the prefixes 10*, 100*, and 1001*. Hugh Hopeful would like
   to cache prefixes instead of entire 32-bit addresses. Hugh’s scheme keeps a set of prefixes in the
   cache (fast memory), in addition to the complete set of prefixes in slow memory. Hugh’s scheme
   first does a best-matching-prefix search in the cache; if a matching prefix is found, the next hop
   of the prefix is used. If no matching prefix is found, a best-matching-prefix search is done for the
   entire database and the resulting prefix cached. Periodically, prefixes that have not been matched
   for a while are flushed from the cache. Alyssa P. Hacker quickly gives Hugh a counterexample to
   show him that his scheme is flawed and that caching prefixes are tricky (if not impossible). Can
   you?
2. Encoding Prefixes in a Constant Length: We said in the text that encoding prefixes like 10*,
   100*, and 1000* in a fixed length could not be done by padding prefixes with zeroes. It clearly can
   be done by padding with zeroes and adding an encoding of the prefix length. We want to study a
   more efficient method.
   • How many possible prefixes on 32 bits can there be?
   • Show how to encode all such prefixes using a fixed length of 33 bits. Make sure that 10*, 100*,
     and 1000* encode to different values.
   • Can you use this fixed-length encoding of prefixes to have the multiple hash tables used in
     Section 11.11 be packed into a single hash table? Why might this help to decrease the chances
     of hash collisions for a given memory size?
3. Quantifying the Benefits of Compressing One-Way Branches:
   • For a unibit trie that does not compress one-way branches, show that the maximum number of
     trie nodes can be O(N · W ), where N is the number of prefixes and W is the maximum prefix
     length. (Hint: Generate a trie that uses log2 N levels to generate N nodes, and then hang a long
     string of N − W nodes from each of the N nodes.)
   • Show that a unibit trie with text strings to compress one-way branches can have at most 2N trie
     nodes and 2N text strings.
   • Extend your analysis to multibit trie nodes with a fixed stride. How would you implement text
     string compression in such tries?
4. Controlled Prefix Expansion: Code up an efficient algorithm that expands a set of prefixes to
   any target set of lengths L1 , . . . , Lk . Check your algorithm using the sample database of Fig. 11.6.
   What is the complexity of your algorithm?
5. Optimal Variable-Stride Trie: Prove that the varied-stride trie of Fig. 11.8 is optimal for a trie
   height of 2. Use the recursive formulation shown in the text.
6. Reducing Memory References in Lulea: The naive approach to counting bits shown in Fig. 11.13
   should take three memory references (to access numSet, to read the appropriate chunk of the
   bitmap, and to access the compressed trie node for the actual information.) Show how to use
   P4a to combine the first two accesses into a single access.
7. Next Node versus Leaf Pushing in Lulea: Before we applied Lulea compression, we first leaf
   pushed the expanded trie of Fig. 11.7. The motivation was to make every entry either a pointer or
   a prefix but not both. Suppose we have a special prefix entry at the top of every trie node; if any

292      Chapter 11 Prefix-match lookups



    entry in a trie node has pointer p and prefix P , we push P to the top of the node pointed to by
    p. Thus we would push the prefix P8 in the 100 entry of the root of Fig. 11.7 to the top of the
    rightmost trie node.
    • We cited leaf pushing as one of the reasons for slow insertion times in the Lulea scheme. Does
      next-node pushing allow incremental insertion for the Lulea scheme?
    • How would you modify trie search to take into account the fact that prefixes can be stored at
      the top of (potentially large) trie nodes? How would this increase the search time (in memory
      accesses) of the Lulea scheme?
 8. CAM Node Compression: Instead of using the Lulea scheme for compression, we could just
    store all the prefixes within a trie node without expansion. If we use small trie nodes (3- or 4-bit
    strides), a chip can potentially read all the entries in a node and internally do a comparison to find
    the best-matching prefix within the node. Describe the details of such a scheme.
 9. Tree Bitmap Algorithm: The tree bitmap algorithm described in the text requires rooting through
    the internal prefix bitmap to decide if there was a matching prefix at a trie node N before moving
    on. This requires a greater access width (to access the internal prefix bitmaps) and more time.
    Consider adding state to the next node in the search path (P12) and one more final memory access
    to avoid this overhead.
10. Multicolumn Binary Search: In Chapter 4 we saw how to efficiently use binary search when
    the identifiers were wide. Explain how to combine this idea with that of binary search on prefixes
    explained in this chapter in order to do IPv6 lookups (up to 128-bit prefixes). How does this scheme
    compare with the other schemes in terms of lookup performance for IPv6?
11. Binary Search with Fast Incremental Updates: (This is difficult.) Find a way to remove all the
    problems of updates to binary search. The key problem is that if a large prefix range R contains lots
    of disjoint prefix ranges R1 , . . . Rk , then the spaces between the ranges Rk must be precomputed
    to map to R. If we now add a new prefix range, R  , that is contained in R but still contains R1
    through Rk , then all the spaces between the ranges Rk must be changed to map to the new range,
    R  . Since k can be O(n), this could lead to a O(n) update. Try to avoid this problem by storing the
    binary search database as a tree and storing information about precomputed prefixes that cover the
    space between ranges as high as possible in the tree, as opposed to storing in the leaves. Details
    can be found in Warkhede et al. (2001).
12. Counterexamples for Binary Search on Prefix Lengths: Even in industry, it is often useful to
    show by counterexample that worst cases can actually exist. This ensures that we are not doing
    unnecessary work, and it also silences people who say that the worst case will never be too bad.
    Imagine that Hugh Hopeful is working for the same startup building an IP lookup chip. The com-
    pany is now considering using binary search on prefix lengths.
    • Suppose we use only markers and no precomputation. This would make insertion a lot faster.
      Hugh Hopeful suggests that backtracking can only lead to a logarithmic number of extra ac-
      cesses. Find an example that leads to linear time.
    • Hugh Hopeful finds that in practice real databases add only 25% extra marker storage, much
      less than the log2 W multiplicative factor that we claimed. This is important because he would
      like to boast of a larger number of prefixes that his chip can handle for the given amount of
      memory. Give a worst-case example to show that we can add log2 W entries per marker.

                                                                            11.17 Exercises         293



13. Rope Search: Binary search on prefix lengths can be improved by what is called rope search in
    Waldvogel et al. (1997). If we ever get a match with some entry M at length m, we only search
    further among the set of lengths corresponding to prefixes that are extensions of M. The basic
    technique we studied earlier will continue to search among all lengths greater than m in the current
    set of lengths R. However, many of the lengths l > m may not have a prefix that is an extension
    of M. Thus this optimization can result in more than halving the set of possible lengths on each
    match. It may not help the worst case, but it can considerably help the average case. Try to work
    out the details of such a scheme. In particular, a naive approach would keep a list of all potentially
    matching lengths (O(W ) space, where W is the length of an address) with each prefix. Find a way
    to reduce the state kept with each marker to O(log W ). Details can be found in Waldvogel et al.
    (1997).
14. Invariant for Binary Search on Prefix Ranges: Designing and proving algorithms that correct via
    invariants is a useful technique even in network algorithmics. The standard invariant for ordinary
    binary search when searching for key K is: “K is not in the table, or K is in the current range R.”
    Standard binary search starts with R equal to the entire table and constantly halves the range while
    maintaining the invariant. Find a similar invariant for binary search on prefix ranges.
15. Semiperfect Hashing: Hardware chips can fetch up to 1000 bits at a time using wide buses.
    Exploit this observation to allow up to X collisions in each hash table entry, where the X colliding
    entries are stored at adjacent locations. Code up a perfect hashing implementation (of 1000 IP
    addresses using a set of random hash functions), and compare the amount of memory needed with
    an implementation based on semiperfect hashing.
16. Removing Redundancies in Lookup Tables: Besides the use of compressed structures, another
    technique to reduce the size of IP lookup tables (especially when the tables are stored in on-chip
    SRAM) is to remove redundancy. One simple example of redundancy is when a prefix P is longer
    than a prefix P  and they both have the same next hop. Which prefix can be removed from the
    table? Can you think of other examples of removing redundancy? How would you implement such
    compression? Draves et al. (1999) describe a dynamic programming algorithm for compression,
    but even simpler alternatives can be effective.
17. Alternative SAIL implementation: Since there are 4 cases considered in the description of SAIL,
    the basic SAIL algorithm uses pivot pushing and an extra lookup to the netx hop array at the pivot
    level to manage with a bitmap (that has only 1 bit and hence 2 possibilities for each bit). Suppose
    we use 2 bits for each possible prefix P at the pivot length. Can we avoid pivot pushing? What are
    the tradeoffs in terms of on-chip memory, speed of lookup and insertion costs.
18. Implementing Lookups in P4: Go to https://github.com/p4lang/ and download the latest P4 com-
    piler and behavioral model and Mininet if necessary. Implement the DXR, SAIL, Tree bitmap, and
    Mashup Algorithms and compare them. Can CAM be used to simplify or make more efficient the
    SAIL and DXR algorithms? Compare these algorithms with respect to a P4 implementation both
    for IPv4 and IPv6.
19. Implementing Tries for Best Matching Prefix: (Due to V. Srinivasan.) The problem is to use
    tries to implement a file name completion routine in C or C++, similar to ones found in many
    shells. Given a unique prefix, the query should return the entire string. For example, with the
    words angle, epsilon, and eagle: Search(a) should return angle, Search(e) should return “No unique
    completion,” Search(ea), Search(eag), etc. should return eagle; and Search(b) should return “No
    matching entries found.” Assume all lowercase alphabets. To obtain an index into a trie array, use:

294   Chapter 11 Prefix-match lookups



  index= charVariable - ‘a’.

  The following definition of a trie node may be helpful.

  \#defineALPHA26
  structTRIENODE
  {
  intcompletionStatus;
  charcompletion[MAXLEN];
  structTRIENODE*next[ALPHA];
  }

  Can other techniques discussed in the text (e.g., binary search) be applied to this problem? Are
  insertion costs significant?

                                                                                                                     CHAPTER


Packet classification
                                                                                                             12
                                                                  A classification is a definition comprising a system of definitions.
                                                                                                            —Friedrich von Schlegel


Traditionally, the post office forwards messages based on the destination address in each letter. Thus
all letters to Timbuctoo were forwarded in exactly the same way at each post office. However, to gain
additional revenue, the post office introduced service differentiation between ordinary mail, priority
mail, and express mail. Thus forwarding at the post office is now a function of the destination address
and the traffic class. Further, with the specter of terrorist threats and criminal activity, forwarding could
even be based on the source address, with special screening for suspicious sources.
    In exactly the same way, routers have evolved from traditional destination-based forwarding devices
to what are called packet classification routers. In modern routers, the route and resources allocated to
a packet are determined by the destination address as well as other header fields of the packet, such as
the source address and TCP/UDP port numbers.
    Packet classification unifies the forwarding functions required by firewalls, resource reservations,
QoS routing, unicast routing, and multicast routing. In classification, the forwarding database of a router
consists of a potentially large number of rules on key header fields. A given packet header can match
multiple rules. So each rule is given a cost, and the packet is forwarded using the least-cost matching
rule.
    The world has changed significantly since the first edition, but most of the changes relevant to packet
classification are a subset of the changes described at the start of Chapter 11 on IP lookups. These are the
significant use of IPv6 (which complicates packet classification), the increasing use of Software Defined
Networks (SDN) and hypervisor switches (Pfaff et al., 2015) to do flexible forwarding using packet
classification instead of simpler IP lookups, and the emergence of Network Function Virtualization
(NFV) which requires software solutions to packet classification. We are grateful to Balajee Vamanan
for helping us with more recent work in packet classification. Despite these technological changes, the
essential ideas have remained.
    This chapter is organized as follows. The packet classification problem is motivated in Section 12.1.
The classification problem is formulated precisely in Section 12.2, and the metrics used to evaluate
rule schemes are described in Section 12.3. Section 12.4 presents simple schemes such as linear search,
tuple space search and TCAMs. Section 12.5 begins the discussion of more efficient schemes by de-
scribing an efficient scheme called grid of tries that works only for rules specifying values of only two
fields. Section 12.6 transitions to general rule sets by describing a set of insights into the classification
problem, including the use of a geometric viewpoint.
    Section 12.7 begins the transition to algorithms for the general case with a simple idea to extend 2D
schemes. A general approach based on divide-and-conquer is described in Section 12.8. This is followed
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00019-1
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                                295

296      Chapter 12 Packet classification



    Table 12.1 Summary of the principles used in the classification algorithms described in
    this chapter.
    Number                            Principle                                       Lookup technique
    P12         Add marker state                                           Rectangle and tuple search
    P2a         Precompute filter info
    P15         Use Dest and SRC tries                                     Grid of tries
    P2a         Precompute switch pointers
    P15         Divide-and-conquer by first doing field lookups            Bit vector, pruned tuple, cross-producting
    P12, 2a
    P11         Exploit lack of general ranges                             Multiple 2D planes
    P4a         Exploit bitmap memory locality                             Bit vector scheme
    P11         Exploit small number of prefixes that match any field      Pruned tuple
    P11a, 4a    Exploit cross product locality                             On-demand cross product
    P1          Avoid redundant cross products                             Equivalent cross-producting


by three very different examples of algorithms based on divide-and-conquer: simple and aggregated
bit vector linear search (Section 12.9), cross-producting (Section 12.10), and RFC, or equivalenced
cross-producting (Section 12.11). Section 12.12 presents the most promising of the current algorithmic
approaches, an approach based on decision trees.
    This chapter will continue to exhibit the set of principles introduced in Chapter 3, as summarized
in Table 12.1. The chapter will also illustrate three general problem-solving strategies: solving simpler
problems first before solving a complex problem, collecting different viewpoints, and exploiting the
structure of input data sets.

  Quick reference guide
  The most important lookup algorithms for an implementor today are as follows. If memory is not an issue, the fastest
  scheme is one called recursive flow classification (RFC), described in Section 12.11. If memory is an issue, a simple
  scheme that works well for classifiers up to around 5000 rules is the Lucent bit vector scheme (Section 12.9). For larger
  classifiers, the best trade-off between speed and memory is provided by decision tree schemes, such as HyperCuts and
  EffiCuts (Section 12.12). For software settings which require fast updates as in Hypervisor switches, then a good solution
  is Tuple Space Search and the improvements implemented in Open Vswitch (Pfaff et al., 2015). Unfortunately, all these
  algorithms are based on heuristics and cannot guarantee performance on all databases. If guaranteed performance is
  required for more than two field classifiers, there is no alternative but to consider hardware schemes such as ternary
  CAMs.
