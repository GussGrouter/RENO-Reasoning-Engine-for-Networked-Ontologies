# Chunk 000002

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Slice: 2.3.1 Endnode architecture
- From: processed/code/network-algorithmics-2-3-1-endnode-architecture.md

---
34       Chapter 2 Network implementation models




FIGURE 2.8
Model of a workstation.


    Many computing benchmarks exhibit temporal and spatial locality; however, a stream of packets
probably exhibits only spatial locality. Thus improving endnode protocol implementations often re-
quires paying attention to cache effects.
    The foregoing discussion should set the stage for the endnode architecture model shown in Fig. 2.8.
The processor, or CPU—e.g., a Pentium or an Alpha—sits on a bus. A bus can be thought of as a
network like an Ethernet, but optimized for the fact that the devices on the bus are close to each other.
The processor interacts with other components by sending messages across the bus.
    The input–output (I/O) devices are typically memory mapped. In other words, even I/O devices like
the network adaptor and the disk look like pieces of memory. For example, the adaptor memory may
be mapped to 100–200 in the memory address space. This allows uniform communication between
the CPU and any device by using the same conventions used to interact with memory. In terms of
networking, a Read (or Write) can be thought of as a message sent on the bus addressed to the memory
location. Thus a Read 100 is sent on the bus, and the device that owns memory location 100 (e.g., the
adaptor) will receive the message and reply with the contents of location 100.
    Modern machines allow direct memory access (DMA), where devices such as the disk or the net-
work adaptor send Reads and Writes directly to the memory via the bus without processor intervention.
However, only one entity can use the bus at a time. Thus the adaptor has to contend for the bus; any
device that gets hold of the bus “steals cycles” from the processor. This is because the processor is
forced to wait to access memory while a device is sending messages across the bus.
    In Fig. 2.8, also notice that the adaptor actually sits on a different bus (system bus or memory bus)
from the bus on which the network adaptor and other peripherals (I/O bus) sit. The memory bus is
designed for speed and is redesigned for every new processor; the I/O bus is a standard bus (e.g., a PCI
bus) chosen to stay compatible with older I/O devices. Thus the I/O bus is typically slower than the
memory bus.
    A big lesson for networking in Fig. 2.8 is that the throughput of a networking application is crucially
limited by the speed of the slowest bus, typically the I/O bus. Worse, the need for extra copies to
preserve operating system structure causes every packet received or sent by a workstation to traverse
the bus multiple times. Techniques to avoid redundant bus traversals are described in Chapter 5.
    Modern processors are heavily pipelined with instruction fetch, instruction decode, data reads, and
data writes split into separate stages. Superscalar and multithreaded machines go beyond pipelining
