# Network Algorithmics — 1.1.1 Endnode bottlenecks Endnodes are the endpoints of the network. They include personal computers and workstations as well (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 31
- Slice: from `1.1.1 Endnode bottlenecks Endnodes are the endpoints of the network. They include personal computers and workstations as well` up to next detected section heading

---

1.1.1 Endnode bottlenecks
Endnodes are the endpoints of the network. They include personal computers and workstations as well
as large servers that provide services. Endnodes are specialized toward computation, as opposed to
networking, and are typically designed to support general-purpose computation. Thus endnode bottle-
necks are typically the result of two forces: structure and scale.
• Structure: To be able to run arbitrary code, personal computers and large servers typically have
  an operating system that mediates between applications and the hardware. To ease the software
  development, most large operating systems are carefully structured as layered software; to pro-
  tect the operating system from other applications, operating systems implement a set of protection
  mechanisms; finally, core operating systems routines, such as schedulers and allocators, are written
  using general mechanisms that target as wide a class of applications as possible. Unfortunately, the
  combination of layered software, protection mechanisms, and excessive generality can slow down
  networking software greatly, even with the fastest processors.
• Scale: The emergence of large servers providing Web and other services causes further performance
  problems. In particular, a large server such as a Web server will typically have thousands of con-
  current clients. Many operating systems use inefficient data structures and algorithms that were
  designed for an era when the number of connections was small.
    Fig. 1.1 previews the main endnode bottlenecks covered in this book, together with causes and so-
lutions. The first bottleneck occurs because conventional operating system structures cause packet data
copying across protection domains; the situation is further complicated in Web servers by similar copy-
ing with respect to the file system and by other manipulations, such as checksums, that examine all the




FIGURE 1.1
Preview of endnode bottlenecks, solutions to which are described in Part 2 of the book.

                                                  1.1 The problem: network bottlenecks                   5



packet data. Chapter 5 describes a number of techniques to reduce these overheads while preserving the
goals of system abstractions, such as protection and structure. The second major overhead is the control
overhead caused by switching between threads of control (or protection domains) while processing a
packet; this is addressed in Chapter 6.
   Networking applications use timers to deal with failure. With a large number of connections, the
timer overhead at a server can become large; this overhead is addressed in Chapter 7. Similarly, network
messages must be demultiplexed (i.e., steered) on receipt to the right end application; techniques to
address this bottleneck are addressed in Chapter 8. Finally, there are several other common protocol
processing tasks, such as buffer allocation and checksums, which are addressed in Chapter 9.
