# network-algorithmics-16-16-2-an-extension-of-min-hash-for-estimating-a-b (chunk 000001)

# Network Algorithmics — 16.16.2 An extension of min-hash for estimating |A                     B| (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 505
- Slice: from `16.16.2 An extension of min-hash for estimating |A                     B|` up to next detected section heading

---

16.16.2 An extension of min-hash for estimating |A                     B|
Now, we describe a slight extension of the min-hash algorithm for solving a different but related count-
ing problem: counting the number of distinct elements
                                                          in the union of two large sets A and B that are
“streaming by,” or in other words estimating |A B|. More precisely, we assume that elements in each
set arrive as a data stream (so that the processor can take only a single pass over it), and the two sets
(streams) A and B are processed by two different processors. Suppose the streams A and B each is
processed using the stated algorithm by the same set of 25 independent hash functions H1 , H2 , · · · ,
H25 , and the resulting arraysare a[1..25] and b[1..25], respectively. The question is whether we can
obtain a good estimate of |A B| from a[1..25] and b[1..25].
    The answer becomes quite obvious when we ask the same question from a different angle. Suppose,
using this algorithm, a processor processes the concatenated stream A||B, which contains all elements
in A followed by all elements in B, and suppose the resulting array is c[1..25]. Our question is how
c[1..25] is related to a[1..25] and b[1..25]. Clearly, for any 1 ≤ i ≤25, we have c[i] = min{a[i], b[i]}
because c[i] is the min-hash value (by the hash function Hi ) of A B, which must equal the smaller
between a[i], the min-hash value of A, and b[i], the min-hash value of B. Once we obtain c[1..25] this

16.16 Counting the number of distinct flows                479

way, we arrive at the following estimator:

             1
                                     |A   B| =                − 1.                                   (16.3)
                                                 MM(c[1..25])
                                                                          
    It will become clear shortly that our “ulterior motive” is to count |A B|, the number of distinct
elements in the intersection of these two sets. However, it is straightforward to obtain the following
estimator using the principle of inclusion and exclusion and the fact that the number of elements in a
set (here A or B) can be counted exactly (using a single counter):

                     
                                    |A   B| = |A| + |B| − |A   B|.                                   (16.4)

While this extension, in hindsight, may appear like a simple mental exercise for readers, it led to a
beautiful solution (Li and Church, 2007), to be described next, to a classical database problem called
association rule mining (Agrawal et al., 1993). While this solution may sound like a “low-hanging fruit”
after we describe it, it actually eluded discovery for more than a decade (from Agrawal et al. (1993)
to Li and Church (2007)).
