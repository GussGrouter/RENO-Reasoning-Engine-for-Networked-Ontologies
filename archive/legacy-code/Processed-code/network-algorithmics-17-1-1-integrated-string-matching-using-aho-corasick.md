# Network Algorithmics — 17.1.1 Integrated string matching using Aho–Corasick (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 519
- Slice: from `17.1.1 Integrated string matching using Aho–Corasick` up to next detected section heading

---

17.1.1 Integrated string matching using Aho–Corasick
Chapter 11 used a trie to search for matching prefixes. Clearly, a trie can also be used to search for
a string that starts at a known position in a packet. Thus Fig. 17.1 contains a trie built on the set
of two strings “babar” and “barney”; both are well-known characters in children’s literature. Unlike in
Chapter 11, the trie is built on characters and not on arbitrary groups of bits. The characters in the text to
be searched are used to follow pointers through the trie until a leaf string is found or until failure occurs.

                                    17.1 Searching for multiple strings in packet payloads                             493



    The hard part, however, is looking for strings that can start anywhere in a packet payload. The
naivest approach would be to assume the string starts at byte 1 of the payload and then traverse the trie.
Then if a failure occurs, one could start again at the top of trie with the character that starts at byte 2.
    However, if packet bytes form several “near misses” with target strings, then for each possible
starting position, the search can traverse close to the height of the trie. Thus if the payload has L bytes
and the trie has maximum height h, the algorithm can take L · h memory references.
    For example, when searching for “babar” in the packet payload shown in Fig. 17.1, the algorithm
jogs merrily down the trie until it reaches the node corresponding to the second “a” in “babar.” At that
point, the next packet byte is a “b” and not the “r” required to make progress in the trie. The naive
approach would be to back up to the start of the trie and start the trie search again from the second byte
“a” in the packet.
    However, it is not hard to see that backing up to the top is obvious waste (P1) because the packet
bytes examined so far in the search for “babab” have “bab” as a suffix, which is a prefix of “babar.” Thus
rather than back up to the top, one can precompute (much as in a grid of tries; see Chapter 12) a failure
pointer corresponding to the failing “b” that allows the search to go directly to the node corresponding
to path “bab” in the trie, as shown by the leftmost dotted arc in Fig. 17.1.
    Thus rather than have the fifth byte (a “b”) lead to a null pointer, as it would in a normal trie, it
contains a failure pointer that points back up the trie. Search now proceeds directly from this node
using the sixth byte “a” (as opposed to the second byte) and leads after seven bytes to “babar.”
    Search is easy to do in hardware after the trie is precomputed. This is not hard to believe because
the trie with failure pointers essentially forms a state machine. The Aho–Corasick algorithm has some
complexity that ensues when one of the search strings, R, is a suffix of another search string, S. How-
ever, in the security context this can be avoided by relaxing the specification (P3). One can remove
string S from the trie and later check whether the packet matched R or S.
    Another concern is the potentially large number of pointers (256) in the Aho–Corasick trie. This can
make it difficult to fit a trie for a large set of strings in cache (in software) or in SRAM (in hardware).
One alternative is to use, say, Lulea-style encoding (Chapter 11) to compress the trie nodes.
