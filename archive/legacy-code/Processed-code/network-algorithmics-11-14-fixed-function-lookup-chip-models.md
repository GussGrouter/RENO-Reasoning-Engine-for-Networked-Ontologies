# Network Algorithmics — 11.14 Fixed Function Lookup-chip models (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 312
- Slice: from `11.14 Fixed Function Lookup-chip models` up to next detected section heading

---

11.14 Fixed Function Lookup-chip models
Classically for Terabit speeds, lookup schemes have been implemented on chips rather than on network
processors. We start in Fig. 11.17 by describing a model of a lookup chip that does search and up-
date, and then describe an alternate model for programmable processors such as Intel’s (aquired from
Barefoot) Tofino-3 (Intel Corporation, 2022). The lookup chip (Fig. 11.17) has a Search and an Update
process, both of which access a common memory that is either on or off chip (or both). The Update
process allows incremental updates and (potentially) does a memory allocation/deallocation and a small
amount of local compaction for every update.
    The actual updates can be done either completely on chip, partially in software, or completely in
software. If a semiconductor company wishes to sell a lookup chip using a complex update algorithm
(e.g., for compressed schemes), it may be wiser also to provide an update algorithm in hardware. If the
lookup chip is part of a forwarding engine, however, it may be simpler to relegate the update process
completely to a separate CPU on the line card.
    The external memory could be SRAM as in Fig. 11.17 but is more likely to be cheaper DRAM
today. Each access to external memory can be fairly wide if needed, even up to 1000 bits. This is quite

286      Chapter 11 Prefix-match lookups



feasible today using a wide bus. The search and update logic can easily process 1000 bits in parallel in
one memory cycle time. Recall that wide word accesses can help, for example, in the tree bitmap and
binary search on values schemes, to reduce search times.
    Search and Update use time multiplexing to share access to the common memory that stores the
lookup database. Thus the Search process is allowed S consecutive accesses to memory, and then the
Update process is allowed K accesses to memory. If S is 20 and K is 2, this allows Update to steal a
few cycles from Search while slowing down Search throughput by only a small fraction. Note that this
increases the latency of Search by K memory accesses in the worst case; however, since the Search
process is likely to be pipelined, this can be considered a small additional pipeline delay.
    The chip has pins to receive inputs for Search (e.g., keys) and Update (e.g., update type, key, result)
and can return search outputs (e.g., result). The model can be instantiated for various types of lookups,
including IP lookups (e.g., 32-bit IP addresses as keys and next hops as results), bridge lookups (48-bit
MAC addresses as keys and output ports as results), and classification (e.g., packet headers as keys and
matching rules as results).
    Each addition or deletion of a key can result in a call to deallocate a block and to allocate a different-
size block. Each allocate request can be in any range from 1 to Max memory words. There is a total of
M words that can be allocated. The actual memory can be either off chip, on chip, or both. Clearly, even
off-chip solutions will cache the first levels of any lookup tree on chip. On-chip memory is attractive
because of its speed and cost. Unfortunately, on-chip memory is limited by current processes which
makes it difficult to support databases of 1 million prefixes without external memory, whether DRAM
or SRAM.
    Internally, the chip is typically heavily pipelined. The lookup data structure is partitioned into sev-
eral pieces, each of which is concurrently worked on by separate stages of logic. Thus the internal
SRAM will likely be broken into several smaller SRAMs that can be accessed independently by each
pipeline stage.
    There is a problem (Sikka and Varghese, 2000) with statically partitioning SRAM between pipeline
stages, because memory needs for each stage can vary as prefixes are inserted and deleted. One pos-
sible solution is to break the single SRAM into a fairly large number of smaller SRAMs that can be
dynamically allocated to the stages via a partial crossbar switch. However, designing such a crossbar at
very high speeds is not easy although such an approach was used in the Procket router (Chung et al.,
2004).
    All the schemes described in this chapter can be pipelined because they are all fundamentally based
on trees. All nodes at the same depth in a tree can be allocated to the same pipeline stage.
