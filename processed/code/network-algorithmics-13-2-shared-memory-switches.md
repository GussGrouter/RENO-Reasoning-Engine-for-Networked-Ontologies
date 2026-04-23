# Network Algorithmics — 13.2 Shared-memory switches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 361
- Slice: from `13.2 Shared-memory switches` up to next detected section heading

---

13.2 Shared-memory switches
Before describing bus- and crossbar-based switches, it is helpful to consider one of the simplest switch
implementations, based on shared memory. Packets are read into a memory from the input links and
read out of memory to the appropriate output links. Such designs have been used as part of time slot
interchange switches in telephony for years. They also work well for networking for small switches.
    The main problem is memory bandwidth. If the chip takes in eight input links and has eight output
links, the chip must read and write each packet or cell once. Thus the memory has to run at 16 times

                                           13.3 Router history: from buses to crossbars                335



the speed of each link. Up to a point, this can be solved by using a wide memory-access width. The
idea is that the bits come in serially on an input link and are accumulated into an input shift register.
When a whole cell has been accumulated, the cell can be loaded into the cell-wide memory. Later they
can be read out into the output shift register of the corresponding link and be shifted out onto the output
link.
    The Datapath switch design (Kanakia, 1999; Keshav, 1997) uses a central memory of 4K cells,
which clearly does not provide adequate buffering. However, this memory can easily be implemented
on-chip and augmented using flow control and off-chip packet buffers. Unfortunately, shared-memory
designs such as this do not scale beyond cell-wide memories because minimum-size packets can be
at most one cell in size. A switch that gets several minimum-size packets to different destinations
can pack several such packets in a single word, but it cannot rely on reading them out at the same
time.
    Despite this, shared-memory switches can be quite simple for small numbers of ports. A great
advantage of shared-memory switches is that they can be memory and power optimal because data is
moved in and out of memory only once. Fabric- or crossbar-based switches, which are described in
the remainder of this chapter, almost invariably require buffering packets twice, potentially doubling
memory costs and power costs. It may even be possible to extend the shared-memory idea to larger
switches via the randomized DRAM interleaving ideas described in Section 13.19.3.
