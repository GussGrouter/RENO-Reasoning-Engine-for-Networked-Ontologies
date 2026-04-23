# network-algorithmics-11-3-2-ternary-content-addressable-memories (chunk 000003)

of wasted storage.) A simple technique to remove this obvious waste (P1) is to compress the one-way
branches.
    In Fig. 11.5 this is done by using a text string (i.e. “01”) to represent the pointers that would have
been followed in the one-way branch. Thus in Fig. 11.5 two trie nodes (containing two pointers apiece)
in the path to P3 have been replaced by a single text string of 2 bits. Clearly, no information has been lost
by this transformation. (As an exercise, determine if there is another path in the trie that can similarly
be compressed.)
    To search for the longest matching prefix of a destination address D, the bits of D are used to trace a
path through the trie. The path starts with the root and continues until search fails by ending at an empty
pointer or at a text string that does not completely match. While following the path, the algorithm keeps
track of the last prefix encountered at a node in the path. When search fails, this is the longest matching
prefix that is returned.
    For example, if D begins with 1110, the algorithm starts by following the 1-pointer at the root to
arrive at the node containing P4. The algorithm remembers P4 and uses the next bit of D (a 1) to follow
the 1-pointer to the next node. At this node, the algorithm follows the 1-pointer to arrive at P2. When
the algorithm arrives at P2, it overwrites the previously stored value (P4) by the newer prefix found
(P2). At this point search terminates because P2 has no outgoing pointers.
    On the other hand, consider doing a search for a destination D  whose first 5 bits are 11000. Once
again, the first 1 bit is used to reach the node containing P4. P4 is remembered as the last prefix
encountered, and the 1 pointer is followed to reach the rightmost node at height 2.
    The algorithm now follows the third bit in D  (a 0) to the text string node containing “01.” Thus
we remember P9 as the last prefix encountered. The fourth bit of D  is a 0, which matches the first bit
of “01.” However, the fifth bit of D  is a 0 (and not a 1 as in the second bit of “01”). Thus the search
terminates with P9 as the longest matching prefix.
    The literature on tries (Knuth, 1973) does not use text strings to compress one-way branches as in
Fig. 11.5. Instead, the classical scheme, called a Patricia trie, uses a skip count. This count records the
number of bits in the corresponding text string, not the bits themselves. For example, the text string
node “01” in our example would be replaced with the skip count “2” in a Patricia trie.
    This works fine as long as the Patricia trie is used for exact matches, which is what they were
used for originally. When search reaches a skip count node, it skips the appropriate number of bits and
follows the pointer of the skip count node to continue the search. Since bits that are skipped are not
compared for a match, Patricia requires that a complete comparison between the searched key and the
entry found by Patricia be done at the end of the search.
    Unfortunately, this works very badly with prefix matching, an application that Patricia tries were
not designed to handle in the first place. For example, in searching for D  , whose first 5 bits are 11000
in the Patricia equivalent of Fig. 11.5, search would skip the last two bits and get to P3. At this point
the comparison will find that P3 does not match D  .
    When this happens, a search in a Patricia trie has to backtrack and go back up the trie searching for
a possible shorter match. In this example, it may appear that search could have remembered P4. But if
P4 was also encountered on a path that contains skip count nodes, the algorithm cannot even be sure of
P4. Thus it must backtrack to check if P4 is correct.
    Unfortunately, the BSD implementation of IP forwarding (Wright and Stevens, 1995) decided to
use Patricia tries as a basis for best matching prefix. Thus the BSD implementation used skip counts;
the implementation also stored prefixes by padding them with zeroes. Prefixes were also stored at the
