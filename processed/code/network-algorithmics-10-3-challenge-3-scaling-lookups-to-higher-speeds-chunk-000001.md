# network-algorithmics-10-3-challenge-3-scaling-lookups-to-higher-speeds (chunk 000001)

# Network Algorithmics — 10.3 Challenge 3: scaling lookups to higher speeds (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 269
- Slice: from `10.3 Challenge 3: scaling lookups to higher speeds` up to next detected section heading

---

10.3 Challenge 3: scaling lookups to higher speeds
First, let’s understand why binary search forwarding does not scale to FDDI speeds. Binary search takes
log2 N memory accesses to look up a bridge database, where N is the size of the database. As bridges
grew popular, marketing feedback indicated that the database size needed to be increased from 8 K to
64 K. Thus using binary search, each search would take 16 memory accesses. Doing a search for the
source and destination addresses using 100-nanosecond DRAM would then take 3.2 microsecond.
    Unlike Ethernet, where small packets are padded to ensure a minimum size of 64 bytes, a minimum-
size packet consisting of FDDI, routing, and transport protocol headers could be as small as 40 bytes.
Given that a 40-byte packet can be received in 3.2 microsecond at 100 Mbps, two binary search lookups
would use up all of the packet-processing budget for a single link, leaving no time for other chores, such
as inserting and removing from link chip queues.
    One simple approach to meet the challenge of wire speed forwarding is to retain binary search but
to use faster hardware (P5). In particular, faster SRAM (Chapter 2) could be used to store the database.
Given a factor of 5–10 decrease in memory access time using SRAM in place of DRAM, binary search
will easily scale to wire speed FDDI forwarding.
    However, this approach is unsatisfactory for two reasons. First, it is more expensive because SRAM
is more expensive than DRAM. Second, using faster memory gets us lookups at FDDI speeds but will
not work for the next speed increment (e.g., Gigabit Ethernet). What is needed is a way to reduce the
number of memory accesses associated with a lookup so that bridging can scale with link technology.
Of the two following approaches to bridge-lookup scaling, one is based on hashing and the other on
hardware parallelism.

10.3.1 Scaling via hashing
In the 1990s DEC decided to build a fast crossbar switch connecting up to 32 links, called the Gi-
gaswitch (Souza et al., 1994). The switch-arbitration algorithms used in this switch will be described
in Chapter 13. This chapter concentrates on the bridge-lookup algorithms used in the Gigaswitch. The
vision of the original designers, Bob Simcoe and Bob Thomas, was to have the Gigaswitch be a switch
connecting point-to-point FDDI links without implementing bridge forwarding and learning. Bridge
lookups were considered to be too complex at 100-Mbps speeds.
    Into the development arena strode a young software designer who changed the product direction.
Barry Spinney, who had implemented an Ada compiler in his last job, was determined to do hardware
design at DEC. Barry suggested that the Gigaswitch be converted to a bridge interconnecting FDDI
local area networks. To do so, he proposed designing an FDDI-to-Gigaswitch network controller (FGC)

10.3 Challenge 3: scaling lookups to higher speeds                      243

FIGURE 10.3
Gigaswitch hashing uses a hash function with a programmable multiplier, a small, balanced binary tree in every hash
bucket, and a backup CAM to hold the rare case of entries that result in more than seven collisions.
