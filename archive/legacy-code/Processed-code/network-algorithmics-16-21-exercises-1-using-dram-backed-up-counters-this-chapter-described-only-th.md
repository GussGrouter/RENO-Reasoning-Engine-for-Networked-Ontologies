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



From denial-of-service to Smurf attacks, hackers that perpetrate exploits have captured both the imag-
ination of the public and the ire of victims. There is some reason for indignation and ire. A survey by
the Computer Security Institute placed the cost of computer intrusions at an average of $970,000 per
company in 2000.
     Thus there is a growing market for intrusion detection, a field that consists of detecting and reacting
to attacks. A 2020 report says that the Intrusion detection market is was USD 4.57 billion in 2020 and is
forecasted to reach USD 9.04 billion by 2028 (Fior Markets, 2020). Further, the report says that roughly
half this market is for network intrusion detection, the topic of this chapter.
     Yet the capabilities of current intrusion detection systems are widely accepted as inadequate, partic-
ularly in the context of growing threats and capabilities. The first problem with some current systems
are that they are slow; but the bigger problem is that they have a high false-positive rate. As a result of
these deficiencies, intrusion detection serves primarily a monitoring and audit function rather than as a
real-time component of a protection architecture on par with firewalls and encryption.
     However, many vendors have introduced real-time intrusion detection systems. If intrusion detection
systems can work in real time with only a small fraction of false positives, they can actually be used to
respond to attacks by either deflecting the attack or tracing the perpetrators.
     Intrusion detection systems (IDSs) have been studied in many forms since Denning’s classic sta-
tistical analysis of host intrusions (Denning, 1987). Today, IDS techniques are usually classified as
either signature detection or anomaly detection. Signature detection is based on matching events to the
signatures of known attacks.
     In contrast, anomaly detection, based on statistical or learning theory techniques, identifies aberrant
events, whether known to be malicious or not. As a result, anomaly detection can potentially detect
new types of attacks that signature-based systems will miss. Unfortunately, anomaly detection systems
are prone to falsely identifying events as malicious. Thus this chapter does not address anomaly-based
methods.
     Meanwhile, signature-based systems are highly popular due to their relatively simple implemen-
tation and their ability to detect commonly used attack tools. The lightweight detection system Snort
(Roesch, 1999) is one of the more popular examples because of its free availability and efficiency.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00025-7
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                489

490      Chapter 17 Network security



    Given the growing importance of real-time intrusion detection, intrusion detection furnishes a rich
source of packet patterns that can benefit from network algorithmics. Thus this chapter samples three
important subtasks that arise in the context of intrusion detection. The first is an analysis subtask, string
matching, which is a key bottleneck in popular signature-based systems such as Snort. The second is a
response subtask, traceback, which is of growing importance given the ability of intruders to use forged
source addresses. The third is an analysis subtask to detect the onset of a new worm (e.g., Code Red)
without prior knowledge.
    These three subtasks only scratch the surface of a vast area that needs to be explored. They were
chosen to provide an indication of the richness of the problem space and to outline some potentially
powerful tools, such as Bloom filters and Aho–Corasick trees, that may be useful in more general
contexts. Worm detection was also chosen to showcase how mechanisms studied earlier in the book
can be combined in powerful ways.
    This chapter is organized as follows. The first few sections explore solutions to the important
problem of searching for suspicious strings in packet payloads. Current implementations of intrusion
detection systems such as Snort (www.snort.org) do multiple passes through the packet to search for
each string. Section 17.1.1 describes the Aho–Corasick algorithm for searching for multiple strings
in one pass using a trie with backpointers. Section 17.1.2 describes a generalization of the classical
Boyer–Moore algorithm, which can sometimes act faster by skipping more bits in a packet.
    Section 17.2 shows how to approach an even harder problem, searching for approximate string
matches. The section introduces two powerful ideas: min-wise hashing and random projections. This
section suggests that even complex tasks such as approximate string matching can plausibly be imple-
mented at wire speeds.
    Section 17.3 marks a transition to the problem of responding to an attack by introducing the IP trace-
back problem. It also presents a seminal solution using probabilistic packet marking. Section 17.4 offers
a second solution, which uses packet logs and no packet modifications; the logs are implemented effi-
ciently using an important technique called a Bloom filter. While these traceback solutions are unlikely
to become deployed when compared to more recent standards, they introduce a significant problem and
invoke important techniques that could be useful in other contexts.
    Section 17.5 explains how algorithmic techniques can be used to extract automatically the strings
used by intrusion detection systems such as Snort. In other words, instead of having these strings be
installed manually by security analysts, could a system automatically extract the suspicious strings?
We ground the discussion in the context of detecting worm attack payloads. Such techniques have
since been known as automatic worm fingerprinting. Section 17.6 describes an early automatic worm
fingerprinting system called EarlyBird and the network algorithmics techniques it uses to scale to high
link and system speeds. Section 17.7 describes Carousel, a network algorithmics solution for another
network security problem that looks deceptively simple but is in fact challenging when the solution has
to scale to high link and system speeds.
    The implementation techniques for security primitives described in this chapter (and the correspond-
ing principles) are summarized in Table 17.1.

                                    17.1 Searching for multiple strings in packet payloads                                491




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
