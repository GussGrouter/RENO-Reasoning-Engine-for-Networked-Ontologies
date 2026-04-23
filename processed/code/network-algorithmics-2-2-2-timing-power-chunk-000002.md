# Chunk 000002

- Source: raw/code/pdf/Network.Algorithmics.pdf
- From: processed/code/network-algorithmics-2-2-2-timing-power.md

---
24       Chapter 2 Network implementation models



balanced binary of 2-input AND gates of height log N . A little thought then shows that the partial
results of the binary tree can be combined in simple ways to get P [j ] for all j < N using the same
binary tree (Wang and Huang, 2000).
    For example, if N = 8, to compute P [8] we compute X = I [0] . . . I [3] and Y = I [4] . . . I [7] and
compute the AND of X and Y at the root. Thus, it is easy to calculate P [5], for instance, using one
more AND gate by computing X · I [4]. Such a method is very commonly used by hardware designers
to replace apparently long O(N) computation chains with chains of length 2 log N . Since it was first
used to speed up carry chains in addition, it is known as carry look-ahead or simply look-ahead. While
look-ahead techniques appear complex, even software designers can master them because, at their core,
they use divide-and-conquer.
