# network-algorithmics-16-16-4-bitmap-sketch-a-worthy-alternative-to-min-hash (chunk 000002)

the same estimation accuracy. The bitmap sketch is extremely simple: an array of bits (bitmap) A[1..n]
initialized to all zero and a hash function h whose range is {1, 2, · · · , n}. For each new data item d, the
bit indexed by the hash value h(d) in A is set to 1. Let n0 be the number of bits in A that remain 0 at the
end of a measurement epoch. Suppose n0 = 0. The estimator for F0 is simply n log(n/n0 ), where the
“log” here is the natural logarithm. When n0 = 0, however, it implies that F0 is too large for the array
A (of size n) to estimate accurately. Using a simple coupon-collector analysis, it can be shown that F0
needs to be at least n log n for n0 = 0 with high probability. For this reason, a bitmap of size n (bits)
is large enough for accurately estimating F0 of magnitude O(n), as long as the constant factor in the
Big-O is small (say, no more than 2 or 3).
    If F0 is close to or exceeds n log n, then most, if not all, of the bits in the bitmap are set to 1. In
this case accurate estimation of F0 is no longer possible from this bitmap. To cope with this problem,
a standard technique is sampling. Sampling works best when we know the approximate range of F0
value, in which case we choose a sampling rate p such that pF0 = O(n) with a small constant factor.
Note that the sampling has to be done consistently in the sense that, if an element is sampled earlier,
then a repetition of this element later in the stream must also be sampled. This consistency requirement
suggests the following hashed sampling similar to that used in trajectory sampling (Duffield and Gross-
glauser, 2000) (described in Section 16.11): Fix a uniform hash function g (unrelated to the other hash
function h) whose range is (0, 1); any data item d is sampled and “inserted” into the bitmap if and only
if g(d) < p.
    In this hashed sampling scheme, there are two sources of estimation errors. The first source is hash
collisions, each of which happens when two or more distinct elements are hashed to the same bit lo-
cation. When n, the size of the bitmap, is fixed, estimation error caused by hash collisions increases
when p increases. The second source is the sampling error, which decreases when p increases. An ob-
vious research question is “how to set the value of p so that the total estimation error caused by both is
statistically minimized?” This question was carefully studied and settled in Zhao et al. (2005).
    In some network measurement applications, however, we do not know even the rough range of F0
to set this sampling rate p properly. This case can be solved using the bitmap sketch augmented by
a multi-resolution sampling technique as follows. We divide (0, 1), the hash space of g, into k > 1
exponentially smaller intervals (0, 1/2), (1/2, 3/4), (3/4, 7/8), · · · , (1 − 2−k+1 , 1 − 2−k ). We also use
k bitmaps, each of size m. For any data item d, if the value of g(d) falls into the first interval (0, 1/2),
then we insert it into the first bitmap; if the value of g(d) falls into the second interval (1/2, 3/4),
then we insert it into the second bitmap, and so on. This way, roughly 1/2, 1/4, · · · , and 1/2k of the
F0 distinct elements are inserted into the first, the second,..., and the kth bitmaps, respectively. If k is

482      Chapter 16 Measuring network traffic
