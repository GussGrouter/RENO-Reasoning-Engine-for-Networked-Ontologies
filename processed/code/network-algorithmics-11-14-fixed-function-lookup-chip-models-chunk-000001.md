# network-algorithmics-11-14-fixed-function-lookup-chip-models (chunk 000001)

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
