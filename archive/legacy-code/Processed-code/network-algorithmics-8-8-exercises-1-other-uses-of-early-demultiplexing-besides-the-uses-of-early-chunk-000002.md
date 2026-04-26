# network-algorithmics-8-8-exercises-1-other-uses-of-early-demultiplexing-besides-the-uses-of-early (chunk 000002)

Our mental image of a musician is often associated with giving a recital, and our image of a researcher
may involve his mulling over a problem. However, musicians spend more time in less glamorous tasks,
such as practicing scales, and researchers spend more time than they wish on mundane chores, such as
writing grants. Mastery of a vocation requires paying attention to many small tasks and not just to a
few big jobs.
    Similarly, tutorials on efficient protocol implementation often emphasize methods of avoiding data-
touching overhead and structuring techniques to reduce control overhead. These, of course, were the
topics covered in Chapters 5 and 6. This is entirely appropriate because the biggest improvements in
endnode implementations often come from attention to such overhead.
    However, having created a zero-copy implementation with minimal context switching—and there is
strong evidence that modern implementations of network appliances have learned these lessons well—
new bottlenecks invite scrutiny. In fact, a measurement study by Kay and Pasquale (1993) shows that
these other bottlenecks can be significant.
    There are a host of other protocol implementation tasks that can become new bottlenecks. Chapters 7
and 8 have already dealt with efficient timer and demultiplexing implementations. This chapter deals
briefly with some of the common remaining tasks: buffer management, checksums, sequence number
bookkeeping, reassembly, and generic protocol processing.
    The importance of these protocol-processing “chores” may be increasing for the following reasons.
First, link speeds in the local network are already at gigabit levels and are going higher. Second, market
pressures are mounting to implement TCP, and even higher-level application tasks, such as Web services
and XML, in hardware. Third, there is a large number of small packets on the Internet for which data
manipulation overhead may not be the dominant factor.
    This chapter is organized as follows. Section 9.1 delves into techniques for managing buffer, that is,
techniques for fast buffer allocation and buffer sharing. Section 9.2 presents techniques for implement-
ing cyclic redundancy checks (CRCs) (mostly at the link level) and checksums (mostly at the transport
level). Section 9.3 deals with the efficient implementation of generic protocol processing, as exempli-
fied by TCP and UDP. Finally, Section 9.4 covers the efficient implementation of packet reassembly.
    The techniques presented in this chapter (and the corresponding principles) are summarized in Ta-
ble 9.1.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00015-4
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                     211

212        Chapter 9 Protocol processing

Table 9.1 Principles used in the various protocol-processing tech-
                     niques discussed in this chapter.
                     Number                           Principle                             Used in
                     P4b         Use linear buffers, not mbuf chains                    Linux sk_buf
                     P4b         Buddy system without coalescing                        BSD 4.2 malloc()
                     P2b         Sequential chunk allocation, lazy chunk creation       J-machine
                     P14         Efficient buffer stealing                              SFQ
                     P13         Dynamic buffer thresholds
                     P2a         CRC multiple bits at a time using table lookup         Many CRC chips
                     P2b         Lazy carry evaluation                                  Fast checksums
                     P12a        Recompute header checksum                              RFC 1624
                     P4c         Compute data link and application CRC                  Infiniband
                     P11         Predict next TCP header                                BSD TCP
                     P3c         Shift fragmentation from router to source              Path MTU
                     P11         Fast fragment reassembly
                     P6          Create efficient specialized routines                  UDP checksums

Quick reference guide
   The first part of Section 9.1 describes a number of buffering strategies, including UNIX mbufs and Linux sk_bufs, as well
   as a variety of efficient memory allocators, such as the Kingsley allocator. Implementors interested in fast cyclic redun-
   dancy check (CRC) algorithms should read Section 9.2.1; those interested in fast IP checksums should read Section 9.2.2.
   The first few pages of Section 9.3 describe the classic TCP processing optimization called header prediction.
