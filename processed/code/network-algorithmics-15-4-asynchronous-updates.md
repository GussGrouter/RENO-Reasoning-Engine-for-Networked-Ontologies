# Network Algorithmics — 15.4 Asynchronous updates (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 468
- Slice: from `15.4 Asynchronous updates` up to next detected section heading

---

15.4 Asynchronous updates
Atomic updates that work concurrently with fast search operations are a necessary part of all the in-
cremental algorithms in Chapters 11 and 10. For example, assume that trie node X points to node Z.
Often, inserting a prefix requires adding a new node Y so that X points to Y and Y points to Z. Since
packets are arriving concurrently at wire speed, the update process must minimally block the search
process. The simplest way to do this without locks is to first build Y completely to point to Z and then,
in a single atomic write, swing the pointer at X to point to Y .
    In general, however, there are many delicacies in such designs, especially when faced with com-
plications such as pipelining. To illustrate the potential pitfalls and the power of correct reasoning,
consider the following example taken from the first bridge implementation.
    In the first bridge product studied in Chapter 10 the bridge used binary search. Imagine we had a
long list of distinct keys B, C, D, E, . . . and with all the free space after the last (greatest key). Consider
the problem of adding a new entry, say, A. There are two standard ways to handle this.
    The first is to mimic the atomic update techniques of databases and keep to two copies of the binary
search table. When A is inserted, search works on the old copy, while A is inserted into a second copy.
Then, in one atomic operation update flips a pointer (which the chip uses to identify the table to be
searched) to the second copy.
    However, this doubles the storage needed, especially if memory is SRAM, and is expensive. Hence,
many designers prefer a second option: create a hole for A by moving all elements B and greater one
position downward.

442        Chapter 15 Routers as distributed systems
