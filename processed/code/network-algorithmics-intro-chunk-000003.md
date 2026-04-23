# Chunk 000003

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 22–23
- From: processed/code/network-algorithmics-intro-p20-24.md

---

prefix lookups, packet classification, switching, and the implementation of measurement and security
primitives. Chapter 1 goes into more detail about the inherent causes of these bottlenecks.
    The fundamental methods that encompass network algorithmics include implementation models
(Chapter 2) and 15 implementation principles (Chapter 3). The implementation models include models
of operating systems, protocols, hardware, and architecture. They are included because the world of
network protocol implementation requires the skills of several different communities, including operat-
ing system experts, protocol pundits, hardware designers, and computer architects. The implementation
models are an attempt to bridge the gaps between these traditionally separate communities.
    On the other hand, the implementation principles are an attempt to abstract the main ideas behind
many specific implementation techniques. They include such well-known principles as “Optimize the
expected case.” They also include somewhat less well-known principles, such as “Combine DRAM
with SRAM,” which is a surprisingly powerful principle for producing fast hardware designs for net-
work devices.
    While Part 1 of the book lays out the methodology of network algorithmics, Part 2 applies the
methodology to specific network bottlenecks in endnodes and servers. For example, Part 2 discusses
copy avoidance techniques (such as passing virtual memory pointers and RDMA) and efficient control
transfer methods (such as bypassing the kernel, as in the VIA proposal, and techniques for building
event-driven servers).
    Similarly, Part 3 of the book applies the methodology of Part 1 to interconnect devices, such as
network routers. For example, Part 3 discusses efficient prefix-lookup schemes (such as multibit or
compressed tries) and efficient switching schemes (such as those based on virtual output queues and
bipartite matching).
    Finally, Part 4 of the book applies the methodology of Part 1 to new functions for security and mea-
surement that could be housed in either servers or interconnect devices. For example, Part 4 discusses
efficient methods to compress large traffic reports and efficient methods to detect attacks.

Organization of the book
This book is organized into four overall parts. Each part is made as self-contained as possible to al-
low detailed study. Readers that are pressed for time can consult the index or Table of Contents for
a particular topic (e.g., IP lookups). More importantly, the opening section of each chapter concludes
with a Quick Reference Guide that points to the most important topics for implementors. The Quick
Reference Guide may be the fastest guide for usefully skimming a chapter.
    Part 1 of the book aims to familiarize the reader with the rules and philosophy of network algorith-
mics. It starts with Chapter 2, which describes simple models of protocols, operating systems, hardware
design, and endnode and router architectures. Chapter 3 describes in detail the 15 principles used as
a cornerstone for the book. Chapter 4 rounds out the first part by providing 15 examples, drawn for
the most part from real implementation problems, to allow the reader a first opportunity to see the
principles in action on real problems.
    Part 2 of the book, called “Playing with Endnodes,” shows how to build fast endnode implemen-
tations, such as Web servers, that run on general-purpose operating systems and standard computer
architectures. It starts with Chapter 5, which shows how to reduce or avoid extra data copying. (Copy-
ing often occurs when network data is passed between implementation modules) and how to increase

---

xxii       Preface
