# network-algorithmics-17-6-earlybird-system-for-worm-detection (chunk 000004)

data-less acknowledgment) and is typically hundreds of bytes long still has a high probability of being
flagged (for further inspection) at least once, yet the resource consumption is reduced by roughly 64
times compared to that without sampling. For example, for a TCP packet with a 512-byte payload, the
probability of not having even a single q-gram of it sampled is only e−8 ≈ 0.00034.
    The second challenge is that hashing a q-gram is quite expensive computationally, when q is mod-
erately large (e.g., q = 40 bytes is used in Singh et al. (2004b)). Depending on the hash function used,
the computational complexity is at least O(q), and usually larger. For example, measurements in Singh
et al. (2004b) show that the average computation time for a hash value is a fraction of a microsec-
ond. Doing this for a packet with a 512-byte-long payload would take hundreds of microseconds. In
comparison, the typical delay incurred by a router to a packet is on the order of microseconds.
    To address the second challenge, EarlyBird makes use of the following insight: the inputs to these
hundreds of hashing operations, given a packet content string s1 s2 · · · sn , are not independent of each
other. Rather, they are “consecutive” q-grams s1 s2 · · · sq , s2 s3 · · · sq+1 , · · · , and sn−q+1 sn−q+2 · · · sn .
    Hence the solution is to use a hash function that is incrementally computable (P12a) so that it is
computationally much cheaper to compute the hash value of the next q-gram from the hash value of
the current q-gram than from scratch. One such hash function is the Rabin fingerprint (Rabin, 1981),
defined as follows.
    A Rabin fingerprint function fx is parameterized by a value x that is chosen randomly but fixed
after being chosen. This function fx maps a q-gram s1 s2 ...sq to s1 x q−1 + s2 x q−2 + · · · + sq−1 x + sq .
Evaluating this polynomial (of x with s1 , s2 , · · · , sq as coefficients) from scratch is relatively compu-
tationally expensive, as it involves q multiplications and q additions even when using the well-known
efficient technique (of rewriting it as (s1 x q−2 + s2 x q−3 + sq−1 ) ∗ x + sq and applying the same trick
recursively to what is inside the parenthesis).
    This function f , however, can be incrementally computed (P12a) as follows. It is not hard to check
that fx (s2 s3 · · · sq+1 ) = s2 x q−1 + s3 x q−2 + ... + sq x + sq+1 = fx (s1 s2 · · · sq ) ∗ x − s1 ∗ x q + sq+1 .
Hence to compute fx (s2 s3 · · · sq+1 ), based on the value of f (s1 s2 · · · sq ), takes only two multiplica-
tions and two additions, assuming the values of x 2 , x 3 ,..., x q have all been precomputed (P2a). This
reduces the computation time of all fingerprints except the first one by more than an order of magnitude,
as shown in Singh et al. (2004b).
    Finally, once a host detects a suspect packet, a q-gram (say α) of which has had its fingerprint fx (α)
flagged by the multistage filter at the host as an elephant, we need to further verify that it is indeed sent
by a spreading worm. If it is, then the q-gram α should appear in packets sent by a large number of
different infected hosts (source IP addresses) within the network; in EarlyBird (Singh et al., 2004b),
this number is called the address dispersion of α. Hence for each suspect packet caught, we need to
estimate its address dispersion. In EarlyBird this is done using a bitmap-based counting scheme (P14)
combined with a multiresolution twist (both described in Section 16.16.4).
