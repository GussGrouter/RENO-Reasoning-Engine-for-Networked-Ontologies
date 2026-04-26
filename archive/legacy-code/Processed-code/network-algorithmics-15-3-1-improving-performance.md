# Network Algorithmics — 15.3.1 Improving performance (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 466
- Slice: from `15.3.1 Improving performance` up to next detected section heading

---

15.3.1 Improving performance
Just as in the previous section, where we striped packets across links when the links were bottlenecks,
many router manufacturers routinely stripe packets across DRAMs within routers. This appears simple:
when packets arrive, they are written into any DRAM not currently being written to. When a packet
leaves, it is read from DRAM, if and only if its DRAM is free. Note that DRAM protocols allow some
limited pipelining of reads or writes to a different bank within the same DRAM, even if the DRAM
itself has not fully completed the previous read or write requests from those different banks within the
same DRAM.
    Unfortunately, while this may work well most of the time or when the system is lightly loaded, it
can work very badly at high loads and for certain access patterns. Some vendors attempt to make such
cases unlikely by adding some speedup, but the approach remains statistical and hard to characterize.
    If worst-case performance is required, especially in situations where there are stringent QoS con-
straints, then such an approach is not correct. In particular, there are several testing firms that can
uncover such flaws in a router. We need a middle way between the correct but expensive solution of
using all SRAM buffers, and the statistical but incorrect solution of striping across DRAM banks.
    A pipelined memory system was proposed in Wang et al. (2010) that can provide robust perfor-
mance in the following sense. This memory system, when receiving a read or write request at time
t, guarantees to complete the request at exactly time t +  (where  is a constant delay), with an
overwhelming probability (say 1 − 10−25 ) under arbitrary memory read or write patterns including the
worst case; it can accommodate a request every SRAM cycle, so it has the same throughput as SRAM.
This statistical guarantee was rigorously proven using worse-case large deviation theory. This memory
system is general-purpose: It can not only support router packet buffers, but also other router or firewall
functions such as the storage, access, and maintenance of network flow state. This memory system has
a shortcoming though: The fixed delay  can be over 1000 SRAM cycles long, or more than several
microseconds long, which is a bit too high for today’s routers and switches. In comparison, the memory
system proposed in Iyer’s thesis provides a tight absolute (not statistical) delay guarantee when used
specifically for router packet buffers. It does so by exploiting the specific memory access patterns of
router packet buffers (P7).
