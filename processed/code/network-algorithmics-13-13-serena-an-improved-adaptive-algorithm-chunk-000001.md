# network-algorithmics-13-13-serena-an-improved-adaptive-algorithm (chunk 000001)

# Network Algorithmics — 13.13 SERENA: an improved adaptive algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 380
- Slice: from `13.13 SERENA: an improved adaptive algorithm` up to next detected section heading

---

13.13 SERENA: an improved adaptive algorithm
SERENA is the best among the several adaptive algorithms proposed in Shah et al. (2002b); Giaccone
et al. (2003). It has the same algorithmic framework and O(N ) computational complexity as sample-
and-compare, yet delivers much better delay performance. Just like sample-and-compare, SERENA
also derives S(t) from S(t − 1) and a random matching R(t). However, there are two key differences
that make it work much better than sample-and-compare. The first difference is that in SERENA R(t)
is not in general a uniform random matching as in sample-and-compare, but is derived from the set of
packet arrivals at time t. This difference results in a statistically heavier R(t) than a uniform random
matching. The second difference is that, through a MERGE procedure, SERENA picks heavy edges
for S(t) from both R(t) and S(t − 1) so that the weight of S(t) can be larger than those of both R(t)
and S(t − 1). This difference allows S(t) to “gain weight” much faster in SERENA than in sample-
and-compare. Next, we describe how R(t) is derived from the packet arrivals and how the MERGE
procedure works.
