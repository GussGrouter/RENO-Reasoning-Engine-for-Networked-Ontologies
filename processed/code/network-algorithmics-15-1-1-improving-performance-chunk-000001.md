# network-algorithmics-15-1-1-improving-performance (chunk 000001)

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
