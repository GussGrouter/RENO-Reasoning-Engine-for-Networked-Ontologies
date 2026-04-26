# network-algorithmics-12-5-3-the-best-of-both-worlds-grid-of-tries (chunk 000001)

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
