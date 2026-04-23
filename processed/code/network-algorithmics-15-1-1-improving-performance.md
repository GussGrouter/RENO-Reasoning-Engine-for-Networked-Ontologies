# Network Algorithmics — 15.1.1 Improving performance (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 458
- Slice: from `15.1.1 Improving performance` up to next detected section heading

---

15.1.1 Improving performance
In Fig. 15.1 if the number of buffers allocated is greater than the product of the line speed and the
round-trip delay (called the pipe size), then transfers can run at the full link speed.
   One problem in real routers is that there are often several different traffic classes that share the link.
One way to accommodate all classes is to strictly partition destination buffers among classes. This can
be wasteful because it requires allocating the pipe size (say, 10 cell buffers) to each class. For a large
number of classes, the number of cell buffers will grow alarmingly, potentially pushing the amount of
on-chip SRAM required beyond feasible limits. Recall that field-programmable gate arrays (FPGAs)
especially have smaller on-chip SRAM limits.

432      Chapter 15 Routers as distributed systems



    But, allocating the full pipe size to all classes at the same time is obvious waste (P1) because, if
every class were to send cells at the same time, each by itself would get only a fraction of the link
throughput. Thus it makes sense to share buffers. The simplest approach to buffer sharing is to divide
the buffer space physically into a common pool together with a private pool for each class.
    A naive method to do so would mark data cells and credits as belonging to either the common or
the private pools to prevent interference between classes. The naive scheme also requires additional
complexity to guarantee that a class does not exceed, say, a pipe size worth of buffers.
    An elegant way to achieve the allow buffer sharing without marking cells is described in Ozveren
et al. (1994). Conceptually, the entire buffer space at the receiver is partitioned so that each class has a
private pool of Min buffers; in addition, there is a common pool of size (B − N ∗ Min) buffers, where
N is the number of classes and B is the total buffer space. Let Max denote the pipe size.
    The protocol runs in two modes: congested and uncongested. When congested, each class is re-
stricted to Min outstanding cells; when uncongested, each class is allowed the presumably larger
amount of Max outstanding cells. All cell buffers at the downstream node are anonymous; any buffer
can be assigned to the incoming cells of any class. However, by carefully restricting transitions between
the two modes, we can allow buffer sharing while preventing deadlock and cell loss.
    To enforce the separation between private pools without marking cells, the sender keeps track of
the total number of outstanding cells S, which is the number of cells sent minus the number of credits
received. Each class i also keeps track of a corresponding counter Si , which is the number of cells
outstanding for class i. When S < N · Min (i.e., the private pools are in no danger of depletion), then
the protocol is said to be uncongested, and every class i can send as long as Si ≤ Max.
    However, when S ≥ N · Min, the link is said to be congested, and each class is restricted to a smaller
limit by ensuring that Si ≤ Min. Intuitively, this buffer-sharing protocol performs as follows. Under a
light load, when there are only a few classes active, each active class gets Max buffers and goes as fast
as it possibly can. Finally, during a continuous period of heavy loading when all classes are active, each
class is still guaranteed Min buffers.
    Hysteresis can be added to prevent oscillation between the two modes. It is also possible to extend
the idea of buffer sharing for credit-based flow control to rate sharing for rate-based flow control using,
say, leaky buckets (Chapter 14).
