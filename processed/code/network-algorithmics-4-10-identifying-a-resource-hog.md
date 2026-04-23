# Network Algorithmics — 4.10 Identifying a resource hog (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 121
- Slice: from `4.10 Identifying a resource hog` up to next detected section heading

---

4.10 Identifying a resource hog
Suppose a device wishes to keep track of resources, like the packet memory allocated to various sources
in a router. The device wants a cheap way to find the source consuming the most memory so that the
device can grab memory back from such a resource hog. Fig. 4.18 shows five sources with their present
resource consumption of 1, 9, 30, 24, and 7 units, respectively. The resource hog is S3.

                                                           4.10 Identifying a resource hog              95




FIGURE 4.18
Finding the source that is a resource hog.


    A simple solution to identify the resource hog is to use a heap. However, if the number of sources is
a thousand or more, this may be too expensive at high speeds. Assume that the numbers that describe
resource usage are integers in the range from 1 to 8000. Thus bucket sort techniques won’t work well
because we may have to search 8000 entries to find the resource hog.
    Suppose, instead, that the device does not care about the exact maximum as long as the result comes
within a factor of 2 (perfect fairness is unimportant as in P3b). For example, in the figure, assume it is
fine to get an answer of 24 instead of 30. This leads to the following problem.

Problem
A software or hardware module needs to keep track of resources required by various users. The module
needs a cheap way to find the user consuming the most resources. Since ordinary heaps are too slow,
the device designers are willing to relax the system requirements (P3b) to be off by a factor of 2. Can
this relaxation in accuracy requirements be translated into a more efficient algorithm?
Hint: Consider using three principles: trading accuracy for computation (P3b), using bucket sorting
(P14), and using table lookups (P4b, P2a).

Solution
Since the answer can be off by a factor of 2, it makes sense to aggregate users whose resources are
within a factor of 2 into the same “resource usage group.” This can be a win if the resulting number of
groups is much smaller than the original number of users; finding the largest group then will be faster
than finding the largest user. This is roughly the same idea behind aggregation in hierarchical routing,
where a number of destinations are aggregated behind a common prefix; this can make routing less
accurate but reduces the number of routing entries. This leads to the following idea (try to work out the
details before you read further).
   Binomial bucketing can be used, as shown in Fig. 4.19, where all users are grouped into buckets
according to resource consumption, where bucket i contains all users whose resource consumption lies
between 2i and 2i+1 − 1. In Fig. 4.19, for instance, users S3 and S4 are both in the range [16, 31] and
hence are in the same bucket.
   Each bucket contains an unsorted list of the resource records of all the users that fall within that
bucket range. Thus in Fig. 4.19, S3 and S4 are in the same list. The data structure also contains a
bitmap, with one bit for every bucket, that is set if the corresponding bucket list is nonempty (Fig. 4.19).
Thus in Fig. 4.19 the bits corresponding to buckets [1,1], [4,7], [8,15], and [16,31] are set, while the bit
corresponding to [2,3] is clear.

96        Chapter 4 Principles in action




FIGURE 4.19
Aggregating users with resource consumption within a factor of 2 leads to a small number of aggregates whose
membership can be represented using a bitmap.


    Thus to find the resource hog, the algorithm simply looks for the bit position i corresponding to the
rightmost bit set in the bitmap. The algorithm then returns the user at the head of the bucket list cor-
responding to position i. Thus in Fig. 4.19 the algorithm would return S4 instead of the more accurate
S3.

Exercises

• How is this data structure maintained? What happens if the resources in a user (e.g., S3) are reduced
  from 30 to 16? What kind of lists is needed for efficient maintenance?
• How large is each bitmap? How can finding the rightmost bit set be done efficiently?
