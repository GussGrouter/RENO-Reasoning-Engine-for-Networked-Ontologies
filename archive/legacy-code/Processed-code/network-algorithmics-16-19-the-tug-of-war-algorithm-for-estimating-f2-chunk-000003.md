# network-algorithmics-16-19-the-tug-of-war-algorithm-for-estimating-f2 (chunk 000003)

486      Chapter 16 Measuring network traffic

p ≥ 3, in terms of space complexity, however, is very high (more precisely at least O(N 1−(2/p) ) as
shown in Alon et al. (1999a)).
     Another salient feature of the ToW sketch is that it is summable in the following sense. Let A and
B be two disjoint data streams. Let C(A) and C(B) be the respective ToW counter values resulting
from processing A    and B using the same hash function H. Clearly, the ToW counter value resulting
from processing
                  A    B is precisely C(A) + C(B). Hence, (C(A) + C(B))2 is an unbiased estimator
of ||A B||2 , the F2 of the union of two streams. Similarly, the ToW sketch is “differentiable” in the
sense that (C(A) − C(B))2 is an unbiased estimator of ||A − B||2 , the F2 of their difference.
     The need for a sketch to be summable and “differentiable” is motivated by the theory and the
applications of distributed data streaming (Feigenbaum et al., 2003). Today’s Internet applications often
generate and collect a massive amount of data at many distributed locations. For example, an ISP
(Internet Service Provider) security monitoring application may require that packet traces be collected
at hundreds (or even thousands) of ingress and egress routers, and the amount of data collected at each
router can be on the order of several terabytes.
     From time to time, various types of queries need to be performed over the union of these data sets.
For example, in this ISP security monitoring application, we may need to query the union of packet trace
data sets at all ingress and egress points to look for globally frequent signatures that may correspond to
certain Internet worms. Given the gigantic and evolving nature of these physically distributed data sets,
it is usually infeasible to ship all the data to a single location for centralized query processing, due to
the prohibitively high communication cost. Therefore, how to execute various types of (approximate)
queries over the union of distributed data sets without physically merging them together has received
considerable research attention in the past two decades.
     Next, we describe a distributed data-streaming problem that has been studied extensively, and its
summable sketch solution, as an example. The problem is to detect global heavy hitters or icebergs,
which are data elements whose aggregate frequency across all these data sets exceeds a prespecified
threshold. The hardness of this problem arises from the fact that a global iceberg may be finely dis-
tributed across all the measurement points so that it does not appear large at any one location. For
example, in security scenarios an adversary may conceal the presence of the iceberg by spreading it
thinly across many different nodes. This precludes the possibility of using a naive algorithm that sim-
ply reports locally frequent elements. On the other hand, it would be prohibitively expensive for every
node to send records for every small fragment to the central server.
     In Zhao et al. (2010), a data-streaming algorithm solution, based on the ToW sketch, was proposed
for the problem of detecting global icebergs. Its key idea is to compute the F2 of the union of the data
streams by exploiting the summability of the ToW sketch. The F2 value is intuitively a good indicator
of global iceberg existence/nonexistence because of its “squaring effect” that significantly magnifies
the skewness of the data (if any). For example, a global iceberg item that is 100 times larger than a
noniceberg item contributes 1002 = 10 000 times more to the total F2 value!
