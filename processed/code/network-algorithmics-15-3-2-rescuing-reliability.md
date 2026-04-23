# Network Algorithmics — 15.3.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 466
- Slice: from `15.3.2 Rescuing reliability` up to next detected section heading

---

15.3.2 Rescuing reliability
The solution advocated in Iyer’s thesis (and first explained in a seminal paper (Sundar et al., 2008)) is to
use SRAM as a cache front-end to an array of DRAM banks. Using clever algorithms and the “staging
SRAM,” it is possible to provably emulate the behavior of a single large SRAM.
    Of course, this is very similar to the use of an SRAM cache for measurement counters we will study
later in the measurement chapter (Section 16.2). This is not surprising because both ideas are described
in Iyer’s thesis (Sundar, 2008). However, in that idea the low order bits of each counter are stored in an
SRAM cache and the high order bits of each counter are stored in DRAM. In this idea, some portion
of the head and tail of each queue are stored in SRAM (for fast read out of packets, and for acceptance

440      Chapter 15 Routers as distributed systems



into a buffer queue respectively) but the vast majority of intermediate packets not in the head or tail are
stored in DRAM.
    To make this idea more precise, however, requires more work. First, we must define the size of the
head and tail queues and show that these numbers are small in comparison to the queue size. Second,
and most importantly, we must define algorithms that decide which packets are read in from SRAM tail
cache to DRAM (on the input side) and which packets are read out from DRAM to SRAM head cache
(on the output side).
    To define the sizes of the head and tail caches required for various algorithms (with different trade-
offs), we need the following notation (Sundar, 2008). First, it seems clear that the ratio between DRAM
and SRAM speeds is a fundamental parameter. If the DRAM access time is 50 nsec and the SRAM
access time is 5 nsec, then 10 = 50/5 packets can arrive to the SRAM during a single DRAM write.
Thus if the memory works in cells of say 64 bytes in length, the cache block (which is also the block
size to be read from and written to DRAM) must be at least 640 bytes.This ratio of DRAM to SRAM
memory speeds expressed in memory units is the first fundamental parameter b.
    The second fundamental parameter is the number of queues Q. Clearly, the more the queues, the
more the possible backlog between SRAM and DRAM. In the worst case, small packets can arrive
to each queue while waiting for a DRAM write. Note that it is possible to do only a single DRAM
write per queue; one cannot batch packets across queues as one can within the same queue. Batching
packets from different queues is in principle possible with complex pointer management when writing
to DRAM. Unfortunately, this defeats the purpose when one reads from DRAM. A read block from
DRAM would now contain data from different queues in varying sizes, and such “scatter gather” reads
cannot cater to the differing per-queue speeds required for dynamic and unpredictable read access
patterns.
    The tail cache is the easiest to understand. Intuitively, the controller gathers up to b bytes per queue
in a tail cache and writes to DRAM in a single larger DRAM block write when possible. Thus a tail
queue size of Qb makes sense. On the other hand, the head cache is more complex, since the controller
has to deal with adversarial read patterns from any queue, and there are a combinatorially large number
of such patterns.
    Surprisingly, if the head cache is slightly larger (proportional to Qb log Q), the algorithm can guar-
antee worst case performance with no starvation at the head cache regardless of which queue is asked
for (assuming, of course, there is data for that queue). Intuitively, again, one might think of something
similar to an earliest deadline first algorithm (but the proof of the worst case bound of Qb log Q still
requires insight). The idea is to replenish from DRAM the head cache with the smallest amount of bytes
first because the adversary may pick on that queue next. The thesis calls this the “most deficited queue
first” algorithm. The actual notion of a deficit is more subtle because of possible pipelining. However,
ignoring pipelining one can think of the queue with the most deficit to be the queue with the least
number of bytes.
    The thesis (Sundar, 2008) and paper (Sundar et al., 2008) also show a series of subtler algorithms
that account for pipelining between DRAM and SRAM, and tradeoff head cache memory for latency.
The general idea is to reduce the amount of head cache maintained on a per queue basis, if one is
prepared to tolerate a larger read latency. A larger read latency allows the algorithm to “look ahead”
into the future queue read patterns and get a better idea of the queues that should be serviced, taking
into account both the current size of the queues in the SRAM head cache and the future request pattern.

                                                                 15.4 Asynchronous updates                441



Further, if it is known that queues do not behave completely adversarially, the head cache size can be
reduced further.
    The distributed memory algorithms described in this section have had a large impact. They were first
commercialized in a startup called Nemo founded by Iyer and McKeown. After Nemo was acquired by
Cisco, it began to considerably impact Cisco routers. By some estimates in Iyer’s thesis Sundar (2008)
distributed memory within Cisco alone is used by several million chips per year in over 7 product lines,
saving hundreds of millions of dollars per year by replacing SRAM with cheap off-chip DRAM, while
allowing queue sizes in the thousands. While the more complex algorithms were used rarely, the simple
most deficited queue algorithm was used in the vast majority of Cisco head cache implementations. For
the tail cache, the simple dynamically allocated cache of size Qb was universally used.
    Besides the memory savings, other advantages include reduced power, reduced pins on ASICs (to
deal with multiple memories), and better utiilization. The better utilization comes from the batching
into blocks of b. A surprising side effect is to eliminate the thorny problem of what happens when
65 byte packets are sent when the internal SRAM cell size is 64 bytes. Such memory fragmentation
becomes less of an issue when a stream of 65 byte packets are batched in a tail cache of size b = 640
bytes (say). A second subtle advantage is that these provably worst case queues eliminate packet drops:
this is crucial for example in the storage market (Sundar, 2008), as well as other applications whose
QoS requirements require strict bounded latency.
