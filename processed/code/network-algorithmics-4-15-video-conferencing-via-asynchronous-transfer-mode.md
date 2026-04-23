# Network Algorithmics — 4.15 Video conferencing via asynchronous transfer mode (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 132
- Slice: from `4.15 Video conferencing via asynchronous transfer mode` up to next detected section heading

---

4.15 Video conferencing via asynchronous transfer mode
In ATM, the network first sets up a VC through a series of switches before data can be sent. Standard
ATM allows one-to-many VCs, where a VC can connect a single source to multiple receivers. Any data
sent by the source is replicated and sent to every receiver in the one-to-many VC.
    Although it is not standardized, it is also easy to have many-to-many VCs, where every endpoint
can be both a source and a receiver. The idea is that when any source sends data, the switches replicate
the data to every receiver. Of course, the main problem in many-to-many VCs is that if two sources talk
at the same time, then the data from the two sources can be arbitrarily interleaved at the receivers and
cause confusion. This is possibly why many-to-many VCs are not supported by standards, though it is
often easy for switch hardware to support many-to-many VCs.
    Fig. 4.28 shows a simple topology consisting of an ATM switch that connects N workstations.
To showcase the bandwidth of the switch, the system designers have designed a videoconferencing
application. The conferencing application can allow users at any of the N workstations to have a video-
conference with each other. The application should bring up a screen (on every workstation in the
conference) that displays at least the current speaker and also plays the speech of the current speaker.
In addition, in the event of a conversation, it is desirable to see the expressions of the participants. The
designers soon run into the following problem.

106      Chapter 4 Principles in action




FIGURE 4.28
A videoconferencing system that uses an ATM switch with the ability to support many-to-many VCs.


Problem
The naivest solution would use up to N 2 point-to-point connections between every pair of participating
workstations. A better solution is shown in Fig. 4.28. It uses up to N many-to-many VCs between
each participating workstation and the other workstations. The video and speech of each workstation
is connected by a one-to-many VC to every other participating workstation. Thus every participating
workstation gets the video output of all participants and the application can choose which one (or ones)
to display. Unfortunately, the ATM switch requires that bandwidth on the switch be statically divided
among the N one-to-many VCs. Given a minimum bandwidth for video quality of Bmin and a total
switch bandwidth of B, this limits the number of participating workstations to be less than B/Bmin . Is
there a more scalable solution?

Hint: Consider exploiting the switch hardware’s ability to support many-to-many VCs (P4c). However,
to prevent confusion, only one source should transmit at a time in any many-to-many VC. Instead
of developing a complex protocol to ensure such a constraint, what hardware can be added (P5) to
ensure this constraint?

Solution
As suggested in the hint, the designers chose to exploit the many-to-many VC capability of the switch
to replace N one-to-many VCs with a constant number of many-to-many VCs. This allowed the fixed
switch bandwidth to scale to a large number of participants. However, this generic idea requires elab-
oration. How many many-to-many VCs should be used? How is the potential confusion caused by
many-to-many VCs resolved? Here are the details of a solution worked out by Jon Turner at Washing-
ton University.
    First, consider the use of a single many-to-many VC named C. A naive solution to the confusion
problem entails a protocol (say, a round-robin protocol) that ensures that only one workstation at a time
connects its video output to C. Such protocols require coordination, and the coordination adds latency
and expense. Instead, as systems thinkers, the designers observed that, at a minimum, only the current
speaker needs to be displayed.

                           4.15 Video conferencing via asynchronous transfer mode                         107




FIGURE 4.29
Replacing N one-to-many VCs with two many-to-many VCs through the use of a speech detector and a simple
hardware state machine at each input.


    Thus the designers added extra hardware (P5) in the form of a speech detector to the input at each
workstation. If the detector detects significant speech activity at a workstation X, then the detector
connects the video input of X to C; otherwise, the video input of X is not connected to C. Since this
hardware was quite cheap, the extra scalability came at a reasonable price.
    Next, the designers observed that keeping a video image of the last speaker provides visual con-
tinuity in the expected case when there is a dialog between two participants. Thus instead of one
many-to-many VC, they used two many-to-many VCs, C and L, one for the current speaker and one
for the last speaker, as shown in Fig. 4.29.

Exercises

• Write pseudocode (using some state variables) for the hardware at each workstation to update its
  connections to C and L. Assume the speech detector output is a function.
• What happens if more than one user speaks at one time? What could you add to the hardware state
  machine so that the application displays something reasonable? For instance, it would be unreason-
  able for the images of the two speakers to be morphed together in this case.

This page intentionally left blank

                                                                                      PART

Playing with endnodes
                                                                                   2
                                       The supreme accomplishment is to blur the line between work and play.
                                                                                           —Arnold Toynbee


The second part of the book deals with endnode algorithmics. This is the application of network algo-
rithmics to building fast protocol implementations at endnodes, especially at servers. If you like, you
can think of it as a systematic collection of techniques for building fast servers. The techniques are ap-
plied mostly in a software setting. Much of it has to do with getting around operating system structure
to enable high-speed data transfers. We study how to reduce the overhead incurred by copying, control
transfer, demultiplexing, timers, and other generic protocol-processing tasks.

This page intentionally left blank

                                                                                                                        CHAPTER


Copying data
                                                                                                                            5
                                                                           Copy from one, it’s plagiarism; copy from two, it’s research.
                                                                                                                      —Wilson Mizner


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




and introduces a well-known technique called integrated layer processing. Section 5.6 broadens the
discussion beyond copying to show that without careful consideration of cache effects, performance
can suffer.
    The world has changed since the first edition of this book and this chapter reflects some of these
changes. The changes include the emergence of servers with multicore CPUs with NUMA (non-
uniform memory access, where groups of cores share an L3 cache), the rapid emergence of 100 Gbps
links, the ubiquity of solid state disks (NVM) that can saturate network links, and recent trends in re-
mote DMA techniques such as the popular RoCE (RDMA over converged Ethernet). We will fit these
trends into our framework, showing that the main ideas of the first edition still hold.
    Although this is the first chapter of the book that is devoted to techniques for overcoming a specific
bottleneck, the techniques are based on the principles described in Part I of the book. The techniques
and the corresponding principles are summarized in Table 5.1.



  Quick reference guide
  The most useful sections for an implementor today are as follows. Section 5.3.1 on remote direct memory access (RDMA)
  describes techniques to avoid memory copying overheads in computing and storage clusters and modern incarnations
  of the idea like RoCE and Fibre Channel. RDMA is only useful for some applications, and so the remaining sections
  concentrate on avoiding copying overheads in general purpose operating systems. Section 5.2.5 summarizes the current
  thinking on zero-copy networking and some modern proposals in Linux that could benefit from a form of precomputation
  called fbufs that is introduced in Section 5.2.3. Section 5.4.3 describes a less radical but effective method called I/O
  splicing to directly connect I/O subsystems and send a file without copying. Finally, Section 5.6.1 describes techniques to
  improve cache performance.

                                                                                        5.1 Why data copies                  113




FIGURE 5.1
Redundant copies involved in handling a GET request at a server.
