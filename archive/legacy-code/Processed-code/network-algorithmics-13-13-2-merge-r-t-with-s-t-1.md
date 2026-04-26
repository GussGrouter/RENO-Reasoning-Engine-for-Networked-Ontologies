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




step is to simply union the two full matchings, viewed as two subgraphs of the complete bipartite graph
                                                                                                         
G(I O), into one that we call the union graph and denote as Sr (I →O) Sg (O →I ) (or Sr Sg
                                                             
in short). In other words, the union graph Sr (I →O) Sg (O →I ) contains the directed edges in both
Sr (I →O) and Sg (O →I ).
     It is a mathematical fact that any such union graph can be decomposed into disjoint directed cy-
cles (Giaccone et al., 2003). Furthermore, each directed cycle, starting from an input port Ii and going
back to itself, is an alternating path between a red edge in Sr and a green edge in Sg , and hence contains
equal numbers of red edges and green edges. In other words, this cycle consists of a red submatching
of Sr and a green submatching of Sg . Then in the second step, for each directed cycle, the MERGE
procedure compares the weight of the red submatching (i.e., the total weight of the red edges in the
cycle), with that of the green submatching, and includes the heavier submatching in the final merged
matching S.
     To illustrate the MERGE procedure by an example, Fig. 13.12 shows the union graph of the two
full matchings shown in Fig. 13.11(a) and (B), respectively. The union graph contains three disjoint
directed cycles that consist of two, six, and eight edges, respectively. In each cycle we pick the heavier
submatching and the resulting merged matching is shown in Fig. 13.11(c). For example, in the third
cycle, the submatching {(I3 , O1 ), (I5 , O4 ), (I4 , O7 ), (I1 , O6 )}, which has a total weight of 8 + 7 + 7 +
5 = 27, is heavier than the other submatching, which has a total weight of 7 + 3 + 1 + 3 = 14. Hence,
it is chosen to be a part of the final matching. The standard centralized algorithm for implementing the
MERGE procedure is to linearly traverse every cycle once, by following the directed edges in the cycle,
to obtain the weights of the green and the red submatchings that comprise the cycle (Giaccone et al.,
2003). Clearly, this algorithm has a computational complexity of O(N ).

356      Chapter 13 Switching
