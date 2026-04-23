# Network Algorithmics — 17.6 EarlyBird system for worm detection (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 533
- Slice: from `17.6 EarlyBird system for worm detection` up to next detected section heading

---

17.6 EarlyBird system for worm detection
EarlyBird (Singh et al., 2004b) is one of the earliest systems for detecting new worms, whose signatures
have never been learned or analyzed, with no or minimum human intervention. A key innovation of
EarlyBird is a fingerprinting technique that is among the earliest for the automated extraction of two
aforementioned features of a new worm: large volume of identical traffic and large number of sources
(IP addresses) sending identical traffic. More specifically, EarlyBird offers a highly scalable solution
to the problem of detecting common substrings in application-layer messages sent by many different
source IP addresses. Such a common substring can be a worm suspect, if it appears in a large number
of application (layer) messages sent from a large number of sources. Since an application message is
often divided into multiple packets for network transmission, we call it an object instead in the rest of
this section to distinguish it from a packet.
    To motivate the EarlyBird solution, we highlight three major challenges in detecting and finger-
printing a common substring in objects, and describe why simple ideas do not work. The first challenge
is that the content of such a common substring is not known in advance and is itself to be learned.
As a result, this problem cannot be simply modeled and solved as the aforementioned string matching
problem (see Section 17.2), since here we do not have a target string to search for.
    The second challenge lies in the fact that, even if we knew the exact target substring, the aforemen-
tioned string matching solutions still would not apply. This is because an object containing the substring
to be searched for can be packetized into multiple packets and it is usually not certain at which byte po-
sition the substring is cut (into packets) for two reasons. First, the typical length of a payload-containing
packet varies across different operating systems. Second, since the application-layer header of an object
(e.g., SMTP header in an email) can vary in length, the location (relative offset from the first byte of
the packet payload) at which the substring appears in an object may vary from one object to another.

                                                    17.6 EarlyBird system for worm detection                       507



    The third challenge lies in the fact that a proposed solution has to scan the content of every packet,
byte by byte, at the full rate of a high-speed link, for such common substrings. Hence any viable solution
has to be simple and take only one quick pass over each packet.
    EarlyBird meets all three challenges by combining a few separate ideas. We now “build” the Early-
Bird solution up one idea at a time. The design of EarlyBird is based on a key observation that if an
n-byte-long worm string s1 s2 · · · sn appears frequently in network objects, then most of its q-byte-long
substrings (called q-grams in the database literature) s1 s2 · · · sq , s2 s3 · · · sq+1 , · · · , sn−q+1 sn−q+2 · · · sn
should also, as long as q > 0 is much smaller than the typical length of a payload-containing packet.
This is because each packetizing cut of an object into packets will break at most q − 1 such q-grams
(into two pieces).
    Based on this observation, the first idea is to search for one or more q-grams that appear frequently
in different packets. Again suppose the content of a packet is b1 b2 · · · bn . The idea is to somehow
record the fact that we have seen each of its n − q + 1 q-grams once. However, the naive solution of
maintaining a hash table of all q-grams seen and their respective counts is not viable, since each such
packet can lead to n − q + 1 different hash nodes being added to the hash table.
    Fortunately, the problem we have at hand is much simpler in two ways. First, here we care only
about those q-grams that occur frequently. Hence it boils down to an elephant (heavy hitter) detec-
tion problem, for which we have many scalable solutions, including those described in Sections 16.7
and 16.17. Among them, the multistage filter scheme described in Section 16.7 is used as the elephant
detection technique in EarlyBird. Here we have applied the principle of avoiding unnecessary generality
(P7).
    Second, we are in general not interested in the exact (byte-by-byte) value of a (frequently occurring)
q-gram. Hence, we can hash each q-gram into a fixed-length integer value, which we call a fingerprint,
for easier processing. Here, we have applied the principle of trading certainty for time (P3a).
    We now describe how a multistage filter is used in EarlyBird for detecting frequently occurring
q-grams. Recall that a multistage filter, shown in Fig. 16.8, employs k > 1 different hash functions
and consists of k equal-sized array of counters. The update procedure, or how the multistage filter
“records” seeing a q-gram s1 s2 · · · sq is straightforward: this q-gram is mapped by the k hash functions
to k aforementioned fingerprints; each fingerprint is considered an index into the corresponding array
of counters and each corresponding counter is incremented by 1.
    The (elephant) detection procedure is also straightforward: when incrementing the k counters that
correspond to a q-gram, if the algorithm finds that all counter values are larger than a certain threshold,
then the packet containing the q-gram is logged for further inspection.
    Two challenges remain to be addressed for this elephant detection approach to work in a high-speed
network environment. The first challenge is that, since a worm string can be thousands of bytes long,
thousands of its q-grams would have to be recorded in the multistage filter and marked as elephants.
This would significantly increase the number of counters in each array for the multistage filter to accu-
rately detect elephants (say to have a low false-positive rate). This would make the multistage filter very
costly, which, as explained earlier, is typically stored in SRAM. This is also unnecessary and wasteful
since, to detect a worm, it suffices to record just one such q-gram.
    To address this challenge, EarlyBird samples over the signature space. The idea is to sample each
fingerprint value with a small probability. For example, in an implementation of EarlyBird described
in Singh et al. (2004b), only fingerprints that end with six 0’s are sampled, resulting in a sampling rate
of 1/64. With the 1/64 sampling, a TCP packet that contains an application-layer payload (i.e., not a

508       Chapter 17 Network security



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
