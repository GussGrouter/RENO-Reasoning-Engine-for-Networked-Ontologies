# Network Algorithmics — 12.5.3 The best of both worlds: grid of tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 335
- Slice: from `12.5.3 The best of both worlds: grid of tries` up to next detected section heading

---

12.5.3 The best of both worlds: grid of tries
The two naive variants of two-dimensional tries pay either a large price in memory (set-pruning tries)
or a large price in time (backtracking search). However, a careful examination of backtracking search
reveals obvious waste (P1), which can be avoided using precomputation (P2a).
    To see the wasted time in backtracking search, consider matching the packet with destination ad-
dress 001 and source address 001 in Fig. 12.6. The search in the destination trie gives D = 00 as the best
match. So the backtracking algorithm starts its search for the matching source prefix in the associated
source trie, which contains rules R4 and R5 . However, the search immediately fails, since the first bit
of the source is 0. Next, backtracking search backs up along the destination trie and restarts the search
in the source trie of D = 0∗, the parent of 00∗.
    But backing up the trie is a waste because if the search fails after searching destination bits 00 and
source bit 0, then any matching rule must be shorter in the destination (e.g., 0) and must contain all the

                                                             12.5 Two-dimensional schemes               309




FIGURE 12.7
Improving the search cost with the use of switch pointers.


source bits searched so far, including the failed bit. Thus backing up to the source trie of D = 0∗ and
then traversing the source bit 0 to the parent of R2 in Fig. 12.6 (as done in backtracking search) is a
waste.
     The algorithm could predict that this sequence of bits would be traversed when it first failed in the
source trie of D = 00. This motivates a simple idea: Why not jump directly to the parent of R2 from
the failure point in the source trie of D = 00∗?
     Thus in the new scheme (Fig. 12.7), for each failure point in a source trie, the trie-building algo-
rithm precomputes what we call a switch pointer. Switch pointers allow search to jump directly to the
next possible source trie that can contain a matching rule. Thus in Fig. 12.7, notice that the source trie
containing R4 and R5 has a dashed line labeled with 0 that points to a node x in the source trie con-
taining {R1 , R2 , R3 }. All the dashed lines between source tries in Fig. 12.7 are switch pointers. Please
distinguish the dashed switch pointers from the dotted lines that connect the destination and source
tries.
     Now consider again the same search for the packet with destination address 001 and source address
001 in Fig. 12.7. As before, the search in the destination trie gives D = 00 as the best match. Search
fails in the corresponding source trie (containing R4 and R5 ) because the source trie contains a path
only if the first source bit is a 1. However, in Fig. 12.7, instead of failing and backtracking, the algorithm
follows the switch pointer labeled 0 directly to node x. It then continues matching from node x, without
skipping a beat, using the remaining bits of the source.
     Since the next bit of the source is a 0, the search in Fig. 12.7 fails again. The search algorithm
once again follows the switch pointer labeled 0 and jumps to node y of the third source trie (associated
with the destination prefix ∗). Effectively, the switch pointers allow skipping over all rules in the next
ancestor source trie whose source fields are shorter than the current source match. This in turn improves
the search complexity from O(W 2 ) to O(W ).
     It may help to define switch pointers more precisely. Call a destination string D  an ancestor of D if
D is a prefix of D. Call D  the lowest ancestor of D if D  is the longest prefix of D in the destination
   

310      Chapter 12 Packet classification



trie. Let T (D) denote the source trie pointed to by D. Recall that T (D) contains the source fields of
exactly those rules whose destination field is D.
    Let u be a node in T (D) that fails on bit 0; that is, if u corresponds to the source prefix s, then the
trie T (D) has no string starting with s0. Let D  be the lowest ancestor of D whose source trie contains
a source string starting with prefix s0, say, at node v. Then we place a switch pointer at node u pointing
to node v. If no such node v exists, the switch pointer is nil. The switch pointer for failure on bit 1 is
defined similarly. For instance, in Fig. 12.7, the node labeled x fails on bit 0 and has a switch pointer to
the node labeled y.
    As a second example, consider the packet header (00∗, 10∗). Search starts with the first source trie,
pointed to by the destination trie node 00∗. After matching the first source bit, 1, search encounters rule
R4 . But then search fails on the second bit. Search therefore follows the switch pointer, which leads
to the node in the second trie labeled with R1 . The switch pointers at the node containing R1 are both
nil, and so search terminates. Note, however, that search has missed the rule R3 = (0∗, 1∗), which also
matches the packet header. While in this case R3 has a higher cost than R1 , in general, the overlooked
rule could have a lower cost.
    Such problems can be avoided by having each node in a source trie maintain a variable storedRule.
Specifically, a node v with destination prefix D and source prefix S stores in storedRule(v) the least-cost
rule whose destination field is a prefix of D and whose source field is a prefix of S. With this precom-
putation, the node labeled with R1 in Fig. 12.7 would store information about R3 instead of R1 if R3
had a lower cost than R1 .
    Finally, here is an argument that the search cost in the final scheme is at most 2W . The time to find
the best destination prefix is at most W . The remainder of the time is spent traversing the source tries.
However, in each step, the length of the match on the source field increases by 1—either by traversing
further down in the same trie or by following a switch pointer to an ancestral trie. Since the maximum
length of the source prefixes is W , the total time spent in searching the source tries is also W . The
memory requirement is O(N W ), since each of the N rules is stored only once, and each rule requires
O(W ) space.
    Note that k-bit tries (Chapter 11) can be used in place of 1-bit tries by expanding each destination or
source prefix to the next multiple of k. For instance, suppose k = 2. Then, in the example of Fig. 12.7,
the destination prefix 0∗ of rules R1 , R2 , R3 is expanded to 00 and 01. The source prefixes of R3 , R4 ,
R6 are expanded to 10 and 11. Using k-bit expansion, a single prefix can expand to 2k−1 prefixes. The
total memory requirement grows from 2N W to N W 2k /k, and so the memory increases by the factor
2k−1 /k. On the other hand, the depth of the trie reduces to W/k, and so the total lookup time becomes
O(W/k).
    The bottom line is that by using multibit tries, the time to search for the best matching rule in an
arbitrarily large two-dimensional database is effectively the time for two IP lookups.
    Just as the grid of tries represents a generalization of familiar trie search for prefix matching, there is
a corresponding generalization of binary search on prefix lengths (Chapter 11) that searches a database
of two field rules in 2W hashes, where W is the length of the larger of the two fields. This is a big gap
from the log W time required for prefix matching using binary search on prefix lengths. In the special
case where the rules do not overlap, the search time reduces even further to log2 W , as shown in Suri
et al. (2001). While these results are interesting theoretically, they seem to have less relevance to real
routers, mostly because of the difficulties of implementing hashing in hardware.

                                                       12.6 Approaches to general rule sets                   311




FIGURE 12.8
Geometric view of the first three rules, R1 , R2 , R3 , in the rule database of Fig. 12.3. For example, the rule
R1 = 0∗, 10∗ is the box whose projection on the destination axis is the range corresponding to 0∗ and whose projec-
tion on the source axis is the range corresponding to 10∗. Note that because R3 = 0∗, 1∗ has the same destination
range as R1 and a source range that strictly includes the range of R1 , the dashed box, R3 , contains the box R1 .
