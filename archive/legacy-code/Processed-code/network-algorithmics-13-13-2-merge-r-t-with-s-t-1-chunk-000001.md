# network-algorithmics-13-13-2-merge-r-t-with-s-t-1 (chunk 000001)

# Network Algorithmics — 13.13.2 Merge R(t) with S(t − 1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 381
- Slice: from `13.13.2 Merge R(t) with S(t − 1)` up to next detected section heading

---

13.13.2 Merge R(t) with S(t − 1)
We now describe the MERGE procedure that allows SERENA to pick heavy edges for S(t) from both
R(t) and S(t − 1). To do so with the best clarity, we need to color-code and orient the edges of R(t)
and S(t − 1), as in Giaccone et al. (2003), as follows. We color all edges in R(t) red and all edges in
S(t − 1) green, and hence, in the sequel, rename R(t) to Sr (“r” for red) and S(t − 1) to Sg (“g” for
green) to emphasize the coloring. We drop the henceforth unnecessary term t here with the implicit
understanding that the focus is on the MERGE procedure at time slot t. We also orient all edges in
Sr as pointing from input ports (i.e., I ) to output port (i.e., O) and all edges in Sg as pointing from
output ports to input ports. We use notations Sr (I →O) and Sg (O →I ) to emphasize this orientation
when necessary in the sequel. Finally, we drop the term t from S(t) and denote the final outcome of the
MERGE procedure as S. An example pair of thus-oriented full matchings Sr (I →O) and Sg (O →I ),
over an 8 × 8 crossbar, are shown in Fig. 13.11(b) and Fig. 13.11(a), respectively.
    We now describe how the two color-coded oriented full matchings Sr (I →O) and Sg (O →I ) are
merged to produce the final full matching S. The MERGE procedure consists of two steps. The first

13.13 SERENA: an improved adaptive algorithm                       355

FIGURE 13.12
Cycles.
