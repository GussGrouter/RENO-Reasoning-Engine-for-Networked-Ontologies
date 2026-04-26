# network-algorithmics-12-5-3-the-best-of-both-worlds-grid-of-tries (chunk 000002)

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
