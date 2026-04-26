# network-algorithmics-16-19-the-tug-of-war-algorithm-for-estimating-f2 (chunk 000002)

16.19 The Tug-of-War algorithm for estimating F2
In this section we describe a data-streaming algorithm for estimating a certain statistic of the flow size
distribution: the second frequency moment of a data stream that is commonly denoted as F2 . Let L be
the set of identifiers of flows that have at least one packet arrival during the measurement epoch. Let cl
denote the frequency of (number of packets in) the flow l during the epoch. The multiset {cl |l ∈ L} is
precisely the flow-size
                         distribution. The second frequency moment (F2 ) of this (traffic) data stream is
defined as F2  l∈L cl2 .
    F2 is an important statistic of a data stream. It was shown in Alon et al. (1999b) that, in databases,
the size of the self-join of a table with itself can be expressed as F2 of the records (rows) in the table
viewed as a data stream. In the networking context, the F2 of a traffic data stream measures how skewed
the traffic volume is toward the large flows. For example, as shown in Zhao et al. (2010), the F2 becomes
extremely large when the traffic volume is heavily concentrated in a small number of elephant flows,
due to the squaring effect (of cl2 for large cl terms).
    A well-known solution to the problem of estimating the F2 of a data stream is the Tug-of-War (ToW)
algorithm (Alon et al., 1999b). This algorithm is easy to explain in the network data stream context.
As in the min-hash algorithm, we need a small number of counters, each of which is associated with
a hash function. For ease of presentation, we only describe, upon the arrival of a packet whose flow
identifier is l, how the algorithm updates a single counter C1 according to an associated hash function
H1 (·). This H1 maps any flow identifier to a random variable that takes the values 1 and −1, each with
probability 0.5. The value of C1 is set to 0 at the beginning of the measurement epoch. The update rule
of the ToW algorithm for counter C1 is extremely simple: C1 := C1 + H1 (l).
    As in the min-hash algorithm, at the end of the measurement epoch, we need to estimate the F2 of
the data stream from the value of C1 . The estimator here is again extremely simple: the square of the
value of C1 . Note that the final value of C1 is l∈L cl ∗ H1 (l). It was proven     in Alon et al. (1999a)
that, as long as the hash function H1 is two-way independent, we have E[C12 ] = l∈L cl2 = F2 . Hence,
roughly speaking, the ToW algorithm has “modulated” the value of F2 into the distribution of the
random variable C1 , and this value can be “demodulated” by measuring E[C12 ]. In statistics terms, C12
is an unbiased estimator of F2 .
    Here, a hash function H(·) is said to be two-way independent, if, for any l1 = l2 , the random vari-
ables H(l1 ) and H(l2 ) are mutually independent; the concept of 4-way independent is similarly defined.
To reason about the accuracy of this estimator, however, knowing only that it is unbiased is not enough.
In addition we need to know its variance. It was proven in Alon et al. (1999a) that, if the hash function
H1 is four-way independent, then the variance of the estimator can be bounded by 2(F2 )2 .
    This variance bound is still quite large, and hence a single counter and estimator is clearly not
enough. As in the min-hash algorithm, when multiple estimators C12 , C22 , · · · , Ck2 are used, the final
estimator is the median of means, which we denote as MM(C12 , C22 , · · · , Ck2 ) as before. Now, the ques-
tion is how many such counters (and hash functions) are enough? It was shown in Alon et al. (1999a)
that, to guarantee an  relative error approximation (of F2 ) with a probability at least 1 − δ, we need
k = log (1/δ)/ 2 counters. Clearly, the number of counters needed here is a constant with respect to
the number of active flows N , unlike in the case of the data-streaming algorithm for estimating the
flow-size distribution where O(N ) counters are generally
                                                             needed. In general, for any integer p > 0, we
                                                              p
can define the pth moment of the data stream as l∈L cl . However, the cost of estimating Fp when
