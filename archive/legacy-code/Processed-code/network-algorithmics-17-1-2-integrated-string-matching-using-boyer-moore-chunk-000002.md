# network-algorithmics-17-1-2-integrated-string-matching-using-boyer-moore (chunk 000002)

FIGURE 17.3
Checking for matching with a random projection of the target string “babar” allows the detecting of similar strings
with substitution errors in the payload.

algorithms add somewhat more overhead due to slightly increased code complexity, which can exhibit
cache effects, as shown in Chapter 3.
    While the code as it currently stands needs further improvement, it is clear that at least the Aho–
Corasick version does produce a large improvement for worst-case traces, which may be crucial for a
hardware implementation. The use of Aho–Corasick and integrated Boyer–Moore can be considered
straightforward applications of efficient data structures (P15).
