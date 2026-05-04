# network-algorithmics-16-21-exercises-1-using-dram-backed-up-counters-this-chapter-described-only-th (chunk 000001)

# Network Algorithmics — 16.21 Exercises 1. Using DRAM-Backed up Counters: This chapter described only the implementation of packet (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 514
- Slice: from `16.21 Exercises 1. Using DRAM-Backed up Counters: This chapter described only the implementation of packet` up to next detected section heading

---

16.21 Exercises
1. Using DRAM-Backed up Counters: This chapter described only the implementation of packet
   counting, not byte counting. Suggest extensions to byte counting.
2. Finding the First Set Bit: Using the techniques and assumptions stated in Chapter 2, find a fast
   parallel implementation of the find-first-bit-set operation for a large (say, of length 1 million) bit
   vector in the context of the counter-management algorithm described in the text.
3. Conservative Update of Multistage Hash Counting: In the multistage filter there is obvious waste
   (P1) in the way counters are incremented. Supposes a flow F , of size 2, hashes into three buckets
   whose counters are 15, 16, and 40. The naive method increases the counters to 17, 18, and 42.
   However, to avoid false negatives, it suffices to increase only the smallest counter to 17 and to
   ensure that all other counters are at least as large. Thus, with this more conservative update strategy
   (Estan and Varghese, 2002), the counters become 17, 17, and 40. Argue why this optimization does
   not cause false negatives and can only improve the false-positive rate.
4. Trajectory Sampling: Extend trajectory sampling to the case where different routers wish to have
   the flexibility to store a different number of packet labels because of different storage capabilities.
   Describe a mechanism that accommodates this and how this affects the potential uses for trajectory
   sampling.
5. Passive Measurement and Denial of Service: In SYN flooding attacks, an attack sends TCP SYN
   packets to a destination D it wishes to attack using a series of fictitious source addresses. When D
   replies to the (often) fictitious host, these packets are not replied to. Thus D accumulates a backlog
   of connections that are “half-open” and eventually refuses to accept new connections. Assume you
   are working at a university and you have an unused Class A address space. How might you use

488      Chapter 16 Measuring network traffic

this address space to infer denial-of-service attacks going on to various destinations on the Internet?
   Assume that attackers pick fake source addresses randomly from the 32-bit address space. More
   details for the curious reader can be found in Moore et al. (2001).
6. Association Rule Mining Using Min-Hash: Let R1 be the min-hash value after every element
   in the multiset {A, B, A, C, D, K, A, B, L, G, A, L, H, B} is processed. Let R2 be the min-hash
   value after every element in the multiset {A, C, K, C, H, K, X, Y, Z} has been processed. Here, we
   assume that a uniform hash function h with range (0, 1) is used in obtaining both R1 and R2 . Answer
   the following three questions.
    a. What is E[R1 ], the expectation of the random variable R1 ?
    b. What is E[R2 ]?
    c. What is E[MI N{R1 , R2 }]?
7. Association Rule Mining: Explain how to extend the min-hash-based solution for mining three-
   way associations (e.g., milk–cereal–banana).

CHAPTER

Network security
                                                                                               17
                                Hacking is an exciting and sometimes scary phenomenon, depending on which side of the
                                                                                battlements you happen to be standing.
                                                                                                   —Marcus J. Ranum
