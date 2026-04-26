# network-algorithmics-15-4-1-improving-performance (chunk 000001)

# Network Algorithmics — 15.4.1 Improving performance (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 469
- Slice: from `15.4.1 Improving performance` up to next detected section heading

---

15.4.1 Improving performance
To reduce memory needs, update must work on the same binary search table on which search works.
To insert element A in, say, Fig. 15.4, update must move the elements B, C, and D one element down.
    If the update and search designers are different, the normal specification for the update designer is
always to ensure that the search process sees a consistent binary search table consisting of distinct keys.
It appears to be very hard to meet this specification without allowing any search to take place until a
complete update has terminated. Since an update can take a long time for a bridge database with 32,000
elements, this is unacceptable.
    Thus one could consider relaxing the specification (P3) to allow a consistent binary search table that
contains duplicates of key values. After all, as long as the table is sorted, the presence of two or more
keys with the same value cannot affect the correctness of binary search.
    Thus the creation of a hole for A in Fig. 15.4 is accomplished by creating two entries for D, then
two entries for C, and then two entries for B, each with a single write to the table. In the last step A is
written in place of the first copy of B.
    To keep the binary search chip simple (see Chapter 10), a route processor was responsible for
updates while the chip worked on searches. The table was stored in a separate off-chip memory; all
three devices (memory, processor, and chip) can communicate with each other via a common bus.
Abstractly, separate search and update processes are concurrently making access to memory. Using
locks to mediate access to the memory is infeasible because of the consequent slowdown of memory.
    Given that the new specification allows duplicates, it is tempting to get away with the simplest
atomicity in terms of reads and writes to memory. Search reads the memory and update reads and
writes; the memory operations of search and update can arbitrarily interleave. Some implementors may
assume that, because binary search can work correctly even with duplicates, this is sufficient.
    Unfortunately, this does not work, as shown in Fig. 15.4.1 At the start of the scenario (leftmost
picture), only B, C, and D are in the first, second, and third table entries. The fourth entry is free.
A search for B begins with the second entry; a comparison with C indicates that binary search should
move to the top half, which consists of only entry 1.
    Next, search is delayed while update begins to go through the process of inserting A by writing
duplicates from the bottom up. By the time update is finished, B has moved down to the second entry.
When search finishes up by examining the first entry, it finds A and concludes (wrongly) that B is not
in the table.
    A simple attempt at reasoning correctly exposes this sort of counterexample directly. The standard
invariant for binary search is that either the element being searched for (e.g., B) is in the current binary
search range or B is not in the table. The problem is that an update can destroy this invariant by moving
the element searched for outside the current range.
    In the bridge application the only consequence of this failure is that a packet arriving at a known
destination may get flooded to all ports. This will worsen performance only slightly but is unlikely to
be noticed by external users!

1 This example is due to Cristi Estan.

15.5 Conclusions             443
