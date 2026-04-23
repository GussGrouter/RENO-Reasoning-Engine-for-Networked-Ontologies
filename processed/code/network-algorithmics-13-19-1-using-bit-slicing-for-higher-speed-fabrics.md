# Network Algorithmics — 13.19.1 Using bit slicing for higher-speed fabrics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 402
- Slice: from `13.19.1 Using bit slicing for higher-speed fabrics` up to next detected section heading

---

13.19.1 Using bit slicing for higher-speed fabrics
The simplest way to cope with link speed increases is to use a faster clock rate to run the switching
electronics. Unfortunately, optical speeds increase exponentially, while ASIC clock rates increase only
at around 10% per year. However, by Moore’s law, the number of transistors placed on a chip doubles
every 18–24 months without a cost increase. Thus the simplest way to cope with link speed increases
is to use parallelism.
    Suppose it were possible to build a crossbar where every link has speed S. Then, to handle links of
speed kS for some constant k, a design could use k crossbar “slices.” For every group of k bits coming
from a link, one bit each is sent to each crossbar slice. Thus each slice sees a reduced link speed of
kS/k = S and thus can be feasibly implemented. Of course, this implies that the reassembly logic can
scale in speed.
    If the bits are distributed to slices in a deterministic fashion (i.e., bit 1 of the first cell goes to slice 1,
bit 2 to slice 2, etc.), the reassembly logic can be simplified because it knows on which slice to expect

376      Chapter 13 Switching



the next bit. However, care must be taken to avoid synchronization errors. The scheduler can make the
same decision for all slices, making the scheduler easy to build.
    The Juniper T-series (Semeria and Gredler, 2001) uses four active switch fabric planes (i.e., slices).
It also uses a fifth plane as a hot-standby for redundancy. Since each plane uses a request–grant mecha-
nism, if a grant does not return within a timeout, a plane failure can be detected. At this point, only the
cells in transit within the failed plane are lost, the failed plane is swapped out for maintenance, and the
standby plane is swapped in.
    While little discussed so far, redundancy and fault tolerance are crucial for large switch designs
because more is at stake. If a small, 8-port router fails, only a few users are affected. But a large, 256-
port-by-256-port router must work nearly always, with internal redundancy, masking out faults. This is
because external redundancy, in terms of a second such router, is too expensive. Most ISPs require core
routers to be NEBS (Network Equipment Building System) (NEBS, 2002) compliant. Typically, large
routers are expected to have at most five minutes of downtime in a year.
