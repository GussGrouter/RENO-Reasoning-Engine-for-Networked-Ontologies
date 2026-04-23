# Network Algorithmics — 11.3.2 Ternary content-addressable memories (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 285
- Slice: from `11.3.2 Ternary content-addressable memories` up to next detected section heading

---

11.3.2 Ternary content-addressable memories
Ternary content-addressable memories (CAMs) that allow “don’t care” bits provide parallel search in
one memory access. Today’s CAMs can search and update in one memory cycle (e.g., 10 nanoseconds)
and handle any combination of 100,000 prefixes. They can even be cascaded to form larger databases.
CAMs, however, have the following issues.
• Density Scaling: One bit in a TCAM requires 10–12 transistors, while an SRAM requires 4–6 tran-
  sistors. Thus TCAMs will also be less dense than SRAMs or take more area. Board area is a critical
  issue for many routers.
• Power Scaling: TCAMs take more power because of the parallel compare. CAM vendors are, how-
  ever, chipping away at this issue by finding ways to turn off parts of the CAM to reduce power.
  Power is a key issue in large core routers.
• Match Arbitration: The match logic in a CAM requires all matching rules to arbitrate so that the
  highest match wins. Older-generation CAMs took around 10 nanoseconds for an operation, but this
  is no longer as much of an issue for modern TCAMs.
• Extra Chips: Given that many routers, such as the Cisco GSR and the Juniper M160, already have
  a dedicated Application Specific Integrated Circuit (ASIC) (or network processor) doing packet

                                                                                     11.4 Unibit tries          259




FIGURE 11.4
Sample prefix database used for the rest of this chapter. Note that the next hops corresponding to each prefix have
been omitted for clarity.


  forwarding, it is tempting to integrate the classification algorithm with the lookup without adding
  CAM interfaces and CAM chips. Note that CAMs typically require a bridge ASIC in addition to the
  basic CAM chip and sometimes require multiple CAM chips.
• Programmable Chips with built-in TCAM: By contrast to the problem of extra chips cited by the
  last bullet (that is caused by separate CAM and packet forwarding chips), a game change in recent
  years has been the emergence of programmable chips capable of performing forwarding with TCAM
  built in. For example, Intel’s Tofino-3 (Intel Corporation, 2022) contains 384 TCAM blocks of size
  44 × 512 each, enough to support a large enterprise or data center but not enough for the backbone
  without some algorithmic tricks.
    In summary, CAM technology is rapidly improving and is supplanting algorithmic methods in
smaller routers. However, for larger core routers that may wish to have databases of a million routes in
the future, it may be better to have solutions (as we describe in this chapter) that scale with standard
memory technologies such as SRAM. SRAM is likely always to be cheaper, faster, and denser than
CAMs. While it is clearly too early to predict the outcome of this war between algorithmic and TCAM
methods, even semiconductor manufacturers have hedged their bets and provide both algorithmic and
CAM-based solutions.



11.4 Unibit tries
It is helpful to start a survey of algorithmic techniques (P15) for prefix lookup with the simplest tech-
nique: a unibit trie. Consider the sample prefix database of Fig. 11.4. This database will be used to
illustrate many of the algorithmic solutions in this chapter. It contains nine prefixes, called P1 to P9,
with the bit strings shown in the figure.
     In practice there is a next hop associated with each prefix omitted from the figure. To avoid clutter,
prefix names are used to denote the next hops. Thus in the figure, an address D that starts with 1
followed by a string of 31 zeroes will match P4, P6, P7, and P8. The longest match is P7.
     Fig. 11.5 shows a unibit trie for the sample database of Fig. 11.4. A unibit trie is based on the simple
algorithmic technique (P15) of divide and conquer based on the bits in the destination address, starting

260       Chapter 11 Prefix-match lookups




FIGURE 11.5
The one-bit trie for the sample database of Fig. 11.4.



with the most significant. A unibit trie is a tree in which each node is an array containing a 0-pointer and
a 1-pointer. At the root all prefixes that start with 0 are stored in the subtrie pointed to by the 0-pointer
and all prefixes that start with a 1 are stored in the subtrie pointed to by the 1-pointer.
    Each subtrie is then constructed recursively in a similar fashion using the remaining bits of the
prefixes allocated to the subtrie. For example, in Fig. 11.5 notice that P1 = 101 is stored in a path
traced by following a 1-pointer at the root, a 0-pointer at the right child of the root, and a 1-pointer at
the next node in the path.
    There are two other fine points to note. In some cases, a prefix may be a substring of another prefix.
For example, P4 = 1* is a substring of P2 = 111*. In that case, the smaller string, P4, is stored inside
a trie node on the path to the longer string. For example, P4 is stored at the right child to the root; note
that the path to this right child is the string 1, which is the same as P4.
    Finally, in the case of a prefix such as P3 = 11001, after we follow the first three bits, we might
naively expect to find a string of nodes corresponding to the last two bits. However, since no other
prefixes share more than the first 3 bits with P3, these nodes would only contain one pointer apiece.
Such a string of trie nodes with only one pointer each is called a one-way branch.
    Clearly one-way branches can greatly increase wasted storage by using whole nodes (containing at
least two pointers) when only a single bit suffices. (The exercises will help you quantify the amount

                                                                              11.4 Unibit tries        261



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

262      Chapter 11 Prefix-match lookups



leaves of the trie, instead of within nodes, as shown in Fig. 11.5. The result is that prefix matching can,
in the worst case, result in backtracking up the trie for a worst case of 64 memory accesses (32 down
the tree and 32 up).
    Given the simple alternative of using text strings to avoid backtracking, doing skip counts is a bad
idea. In essence, this is because the skip count transformation does not preserve information, while
the text string transformation does. However, because of the enormous influence of BSD, a number of
vendors and even other algorithms (e.g., Ref. Nilsson and Karlsson, 1998) have used skip counts in
their implementations.
