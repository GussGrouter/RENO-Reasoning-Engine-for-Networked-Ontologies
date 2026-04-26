# network-algorithmics-17-6-earlybird-system-for-worm-detection (chunk 000002)

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
