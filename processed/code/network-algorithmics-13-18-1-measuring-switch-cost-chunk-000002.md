# network-algorithmics-13-18-1-measuring-switch-cost (chunk 000002)

Metric #2: the complexity of matching computation
Another cost to consider in scaling the switch sizes is the computational complexity of the match-
ing computations involved. As shown earlier, the total time complexity of computing a good crossbar
schedule (bipartite matching) is at least O(N ) (in the case of SERENA) and can go all the way up to
O(N 2.5 log W ) (in the case of MWM), for a switch with N input/output ports. Hence, when the size
N of a switch grows larger and larger, it becomes increasingly difficult to compute schedules for its
underlying (monolithic) crossbar at line rates (say a packet every eight nanoseconds). This time com-
plexity challenge, coupled with the need to reduce the number of crosspoints as explained previously,
has naturally led researchers and the industry to the following divide-and-conquer approach (P15).
