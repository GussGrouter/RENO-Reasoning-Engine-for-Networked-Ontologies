# network-algorithmics-16-21-exercises-1-using-dram-backed-up-counters-this-chapter-described-only-th (chunk 000004)

Quick reference guide
  Sections 17.1.1 and 17.1.2 show how to speed up searching for multiple strings in packet payloads, a fundamental oper-
  ation for a signature-based IDS. The Aho–Corasick algorithm of Section 17.1.1 can easily be implemented in hardware.
  While the traceback ideas in Section 17.4 are unlikely to be useful in the near future, the section introduces an important
  data structure, called a Bloom filter, for representing sets and also describes a hardware implementation. Bloom filters
  have found a variety of uses and should be part of the implementor’s bag of tricks. Section 17.5 explains how signa-
  tures for attacks can be automatically computed (i.e., fingerprinted), reducing the delay and difficulty required to have
  humans generate signatures. Section 17.6 describes EarlyBird, an early system that learns worm fingerprints. Section 17.7
  describes Carousel.

Table 17.1 Principles used in the implementation of the various
                    security primitives discussed in this chapter.
                    Number                      Principle                                    Used in
                     P15     Integrated string matching using Aho–Corasick                    Snort
                    P3a, 5a Approximate string match using min-wise hashing                 Altavista
                      P3a    Path reconstruction using probabilistic marking              Edge sampling
                      P3a       Efficient packet logging via Bloom filters                    SPIE
                    P7, P3a   Worm detection by detecting frequent content                  EarlyBird
                     P12a                 Compute incrementally
                      P2a            Precompute x 2 , x 3 , . . . , and x q
                     P14               Use bitmap-based counting
