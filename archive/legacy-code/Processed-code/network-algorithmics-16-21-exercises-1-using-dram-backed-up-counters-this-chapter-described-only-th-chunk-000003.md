# network-algorithmics-16-21-exercises-1-using-dram-backed-up-counters-this-chapter-described-only-th (chunk 000003)

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
