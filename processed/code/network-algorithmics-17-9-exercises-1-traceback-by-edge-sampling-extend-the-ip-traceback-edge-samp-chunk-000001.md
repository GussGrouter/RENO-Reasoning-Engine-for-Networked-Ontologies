# network-algorithmics-17-9-exercises-1-traceback-by-edge-sampling-extend-the-ip-traceback-edge-samp (chunk 000001)

# Network Algorithmics — 17.9 Exercises 1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 538
- Slice: from `17.9 Exercises 1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space` up to next detected section heading

---

17.9 Exercises
1. Traceback by edge sampling: Extend the IP traceback edge-sampling idea to reduce the space
   required. As described in the text, try to do this by chopping the node ID required in the base
   scheme into smaller (say, 8-bit) fragments. It may help to consider each of the fragment IDs to be
   the IDs of four virtual nodes that are housed in a single physical node, thus effectively extending the
   path and the number of samples needed for reconstruction.
2. Bloom filters and trajectory sampling: Can you use Bloom filters to improve the label storage
   required by trajectory sampling in Chapter 16? Explain.
3. Sampling and packet logging: Can you use packet sampling to reduce the amount of memory
   required by the logging traceback solution? What are the disadvantages and advantages?
4. Traceback by packet logging: Why does the implementation in Fig. 17.8 go through the indirection
   of a hash to 32 bits (as in trajectory sampling) and then to a Bloom filter?

512      Chapter 17 Network security

5. Aho–Corasick as a state machine: In many applications one may wish to ignore certain padding
   characters that can be inserted by an intruder to make strings hard to detect. How might you extend
   Aho–Corasick to ignore these padding characters while searching for suspicious strings?
6. Resemblance and min-wise hashing: Generalize the Broder methods to approximately search for
   multiple strings and return the string with the highest resemblance.
7. Approximate matching and worm detection: Could the methods for approximate search general-
   ize to detecting worms that mutate?

CHAPTER

Conclusions
                                                                                                    18
                                                                           The end of a matter is better than its beginning.
                                                                                                 —Ecclesiastes, The Bible
