# network-algorithmics-16-16-1-the-min-hash-algorithm (chunk 000001)

# Network Algorithmics — 16.16.1 The min-hash algorithm (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 504
- Slice: from `16.16.1 The min-hash algorithm` up to next detected section heading

---

16.16.1 The min-hash algorithm
The min-hash algorithm, also called min-wise hash in a related but different context of locality-sensitive
hashing (Indyk et al., 1997), works as follows. Assume H is a hash function that maps the ID of an
element into a real number uniformly distributed in the open interval (0, 1). The lossy data structure in
this case is very simple. For all data items d1 , d2 , · · · in the data stream, we only maintain, in a variable
V , a so-called min-hash value: the minimum among their hash values H(d1 ), H(d2 ), · · · . The actual
algorithm is, for each data item di , to compare H (di ) with the value of the min-hash variable V seen
so far. The value V is clearly a random variable whose randomness comes from both the hash function
H and the data items d1 , d2 , · · · .
    Suppose, after the entire data stream has passed, the value of the min-hash variable is V = v. This
value v provides a good amount of information concerning the number of distinct elements in the data
stream, which we denote as N . Any statistics book that has a section on order statistics (e.g., Section
5.4 in Casella and Berger (2001)) proves that E[V ] = N 1+1 . Hence, N = E[V          1
                                                                                        ] − 1. Replacing E[V ]
(the first moment of V ) by the observed (sample) value v, we obtain an estimator of N , denoted as N̂ ,
as
                                                        1
                                                 N̂      − 1.                                           (16.1)
                                                        v

478      Chapter 16 Measuring network traffic
