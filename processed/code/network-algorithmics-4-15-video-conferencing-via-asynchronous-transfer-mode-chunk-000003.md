# network-algorithmics-4-15-video-conferencing-via-asynchronous-transfer-mode (chunk 000003)

Imagine an office where every letter received is first sent to shipping and receiving. Shipping and
receiving opens the letter, figures out which department it is meant for, and makes a photocopy for
their records. They then hand it to the security department, which pores over every line of the letter,
looking for signs of industrial espionage. To maintain an audit trail for possible later use, the security
department also makes a photocopy of the letter for good measure. Finally, the letter, somewhat the
worse for wear, reaches the intended recipient in personnel.
    You would probably think this a pretty ludicrous state of affairs, worthy to be featured in a Charlie
Chaplin movie. But then you might be surprised to learn that early Web servers and computers routinely
made a number of extra copies of received and sent messages. Unlike photocopies, which take up only
a small amount of paper, power, and time, extra copying in a computer consumes two precious re-
sources: memory bandwidth and memory itself. Ultimately, if there are k copies involved in processing
a message in a Web server, the throughput of the Web server can be k times slower.
    Thus this chapter will focus on removing the obvious waste (P1) involved in such unnecessary
copies. A copy is unnecessary if it is not imposed by the hardware. For example, the hardware does
require copying bits received by an adaptor to the computer memory. However, as we shall see, there is
no essential reason (other than those imposed by conventional operating system structuring) for copying
between application and operating system buffers. Eliminating redundant copies allows the software to
come closer to realizing the potential of the hardware, one of the goals of network algorithmics.
    This chapter will also briefly talk about other operations (such as checksumming and encryption)
that touch all the data in the packet and other techniques to more closely align protocol software to
hardware constraints, such as bus bandwidths and caches. While we will briefly repeat some of the
relevant operating systems and architectural facts, it will help the reader to be familiar with endnode
architecture and operating system models of Chapter 2. In summary this chapter surveys techniques for
reducing the costs of data manipulation without sacrificing modularity and without major changes to
operating system design.
    This chapter is organized as follows. Section 5.1 describes why and how extra data copies occur.
Section 5.2 describes a series of techniques to avoid copies by local restructuring of the operating
system and network code at an endnode. Section 5.3 shows how to avoid both copy and control overhead
for large transfers using remote direct memory access (DMA) techniques that involve protocol changes.
    Section 5.4 broadens the discussion to consider the file system in, say, a Web server and it shows
how to avoid wasteful copies between the file cache and the application. Section 5.5 broadens the
discussion to consider other operations that touch all the data, such as checksumming and encryption,
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00011-7
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                                  111

112      Chapter 5 Copying data

Table 5.1 Techniques for copy avoidance and cache efficiency that are
                 discussed in this chapter, together with the corresponding principles.
                 Number                             Principle                                   Used in
                 P13         Memory location (on adaptor) as degree of freedom              Afterburner
                 P2b         Lazy copying using copy-on-write                               Mach
                 P11a        Cache VM mappings per path                                     Solaris fbufs
                 P7          Uniform fbuf space across processes
                 P10         Pass buffer name and offset in packet                          RDMA systems
                 P4          VM mapping to avoid copies in cache and application            Flash
                 P11a        Cache VM mappings per path                                     Flash-lite
                             Buffer sequence numbers enable checksum caching
                 P6          New system call that splices I/O                               Sendfile()
                 P1          Avoid repeated memory access across manipulations              ILP
                 P13         Layout code to minimize I-cache misses                         x-kernel
                 P13         Layer processing order as degree of freedom                    LDRP
