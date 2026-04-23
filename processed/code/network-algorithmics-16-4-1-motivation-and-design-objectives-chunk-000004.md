# network-algorithmics-16-4-1-motivation-and-design-objectives (chunk 000004)

ters”. The j th subcounter, j ∈ [1, p]
                                     (from     the least significant bits to the most significant bits) has
                                         p
wj bits, such that 0 < wj ≤ L and j =1 wj = L. To save space, for each counter, BRICK maintains
just enough of its subcounters to hold its current value. In other words, counters with values no more
than 2w1 +w2 +···+wi will not have its (i + 1)th, . . . , pth subcounters stored in BRICK. For example, if
w1 = 5, any counter with a value less than 25 = 32 will only be allocated a memory entry for its first
subcounter. Consider the example shown in Fig. 16.5(A) with k = 8 counters in a bucket. Only C1 and
C5 require more than their first subcounters. Such an on-demand allocation requires us to link together
all subcounters of a counter, which we achieve using a simple and memory-efficient bitmap indexing
scheme called rank indexing. Rank indexing enables efficient lookup and efficient expansion (when
counter values exceed certain thresholds after increments), which will be discussed in detail next.
    Each bucket contains p subcounter arrays A1 , A2 , . . ., Ap to store the 1st, 2nd, . . ., pth sub-counters
(as needed) of all k counters in the bucket. How many entries should be allocated for each array Ai ,
denoted as ki , turns out to be a nontrivial statistical optimization problem. On the one hand, to save
memory, we would like to make k2 , k3 , . . ., kp (k1 is fixed as k) as small as possible. On the other hand,
when we encounter the unlucky situation that we need to exceed any of these limits (say for a certain d,
we have more than kd counters in a bucket that have values larger than or equal to 2w1 +w2 +···+wi−1 ), then
we will have a “bucket overflow” that would require that all counters inside the bucket be relocated to
an additional array of full-size buckets with fixed worst-case width L for each counter. Given the high
cost of storing a duplicate bucket in the full-size array, we would like to choose larger k2 , . . . , kp to
make this probability as small as possible. For the example shown in Fig. 16.5(B), the allocation for
A1 , A2 , and A3 are k1 = k = 8, k2 = 3, and k3 = 1, respectively. Observe that the number of entries
is decreasing exponentially as we go to the higher subcounter arrays. In Hua et al. (2008b) extremely
tight tail bounds were developed on the overflow probability that can be used to guide the choosing of
parameters {ki }2≤i≤p and {wi }1≤i≤p−1 to achieve near-optimal tradeoffs between these two conflicting
issues and minimize the overall memory consumption.

Indexing for efficiently locating a counter
A key innovation in the BRICK data structure is an indexing scheme that allows for the efficient iden-
tification of the locations of the subcounters across the different subcounter arrays for some counter
Ci . In particular, for Ci , its d subcounters Ci,1 , . . . , Ci,d are spread across A1 , . . . , Ad at locations

16.5 Extending BRICK for maintaining associated states                       461
