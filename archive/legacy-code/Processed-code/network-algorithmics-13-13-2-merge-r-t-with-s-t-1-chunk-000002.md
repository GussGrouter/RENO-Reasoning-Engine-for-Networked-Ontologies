# network-algorithmics-13-13-2-merge-r-t-with-s-t-1 (chunk 000002)

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
