# Network Algorithmics — 17.1.2 Integrated string matching using Boyer–Moore (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 520
- Slice: from `17.1.2 Integrated string matching using Boyer–Moore` up to next detected section heading

---

17.1.2 Integrated string matching using Boyer–Moore
The exercises at the end of Chapter 3 suggest that the famous Boyer–Moore (Boyer and Moore, 1977)
algorithm for single-string matching can be derived by realizing that there is an interesting degree of
freedom that can be exploited (P13) in string matching: one can equally well start comparing the text
and the target string from the last character as from the first.
    Thus in Fig. 17.2 the search starts with the fifth character of the packet, a “b,” and matches it to the
fifth character of, say, “babar” (shown below the packet), an “r.” When this fails, one of the heuristics
in the Boyer–Moore algorithm is to shift the search template of “babar” two characters to the right to
match the rightmost occurrence of “b” in the template.1 Boyer–Moore’s claim to fame is that in practice
it skips over a large number of characters, unlike, say, the Aho–Corasick algorithm.
    To generalize Boyer–Moore to multiple strings, imagine that the algorithm concurrently compares
the fifth character in the packet to the fifth character, “e,” in the other string, “barney” (shown above


1 There is a second heuristic in Boyer–Moore (Cormen et al., 1990), but studies have shown that this simple Horspool variation
works best in practice.

494       Chapter 17 Network security




FIGURE 17.2
Integrated Boyer–Moore by shifting a character.



the packet). If one were only doing Boyer–Moore with “barney,” the “barney” search template would
be shifted right by four characters to match the only “b” in barney.
    When doing a search for both “barney” and “babar” concurrently, the obvious idea is to shift the
search template by the smallest shift proposed by any string being compared for. Thus in this example
we shift the template by two characters and do a comparison next with the seventh character in the
packet.
    Doing a concurrent comparison with the last character in all the search strings may seem inefficient.
This can be taken care of as follows. First, chop off all characters in all search strings beyond L, the
shortest search string. Thus in Fig. 17.2 L is 5 and “barney” is chopped down to “barne” to align in
length with “babar.”
    Having aligned all search string fragments to the same length, now build a trie starting backward
from the last character in the chopped strings. Thus in the example of Fig. 17.2 the root node of the trie
would have an “e” pointer pointing toward “barne” and an “r” pointer pointing towards “babar.” Thus
comparing concurrently requires using only the current packet character to index into the trie node.
    On success, the backward trie keeps being traversed. On failure, the amount to be shifted is precom-
puted in the failure pointer. Finally, even if a backward search through the trie navigates successfully
to a leaf, the fact that the ends may have been chopped off requires an epilogue, in terms of checking
that the chopped-off characters also match. For reasonably small sets of strings, this method does better
than Aho–Corasick.
    The generalized Boyer–Moore was proposed by Commentz-Walter (1979). The application to in-
trusion detection was proposed concurrently by Coit et al. (2001) and Fisk and Varghese (2001). The
Fisk implementation (Fisk and Varghese, 2001) was ported to Snort at one stage.
    Unfortunately, the performance improvement of using either Aho–Corasick or the integrated Boyer–
Moore is minimal because many real traces (Coit et al., 2001; Fisk and Varghese, 2001) have only a
few packets that match a large number of strings, enabling the naive method to do well. In fact, the new

                                                            17.2 Approximate string matching                   495




FIGURE 17.3
Checking for matching with a random projection of the target string “babar” allows the detecting of similar strings
with substitution errors in the payload.


algorithms add somewhat more overhead due to slightly increased code complexity, which can exhibit
cache effects, as shown in Chapter 3.
    While the code as it currently stands needs further improvement, it is clear that at least the Aho–
Corasick version does produce a large improvement for worst-case traces, which may be crucial for a
hardware implementation. The use of Aho–Corasick and integrated Boyer–Moore can be considered
straightforward applications of efficient data structures (P15).
