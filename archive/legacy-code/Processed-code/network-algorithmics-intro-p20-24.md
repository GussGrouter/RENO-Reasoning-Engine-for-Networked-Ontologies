# Network Algorithmics — intro slice (PDF pages 20–24)

- Source: 
- Source: `raw/code/pdf/Network.Algorithmics.pdf`
- Extraction: `pdftotext -f 20 -l 24 -layout`

---

## PDF page 20

Preface

Computer networks have become an integral part of society. We take for granted the ability to transact
commerce over the Internet and that users can avail themselves of a burgeoning set of communication
methods, which range from file sharing to Web logs. However, for networks to take their place as part
of the fundamental infrastructure of society, they must provide performance guarantees.
     We take for granted that electricity will flow when a switch is flicked and that telephone calls
will be routed on Mother’s Day. But the performance of computer networks such as the Internet is
still notoriously unreliable. While there are many factors that go into performance, one major issue
is that of network bottlenecks. There are two types of network bottlenecks: resource bottlenecks and
implementation bottlenecks.
     Resource bottlenecks occur when network performance is limited by the speed of the underlying
hardware; examples include slow processors in server platforms and slow communication links. Re-
source bottlenecks can be worked around, at some cost, by buying faster hardware. However, it is quite
often the case that the underlying hardware is perfectly adequate but that the real bottleneck is a de-
sign issue in the implementation. For example, a Web server running on the fastest processors may
run slowly because of redundant data copying. Similarly, a router with a simple packet classification
algorithm may start dropping packets when the number of ACL rules grows beyond a limit, though it
keeps up with link speeds when classification is turned off. This book concentrates on such network
implementation bottlenecks, especially at servers and routers.
     Beyond servers and routers, new breeds of networking devices that introduce new performance
bottlenecks are becoming popular. As networks become more integrated, devices such as storage area
networks (SANs) and multimedia switches are becoming common. Further, as networks get more com-
plex, various special-purpose network appliances for file systems and security are proliferating. While
the first generation of such devices justified themselves by the new functions they provided, it is be-
coming critical that future network appliances keep up with link speeds.
     Thus the objective of this book is to provide a set of techniques to overcome implementation bottle-
necks at all networking devices and to provide a set of principles and models to help overcome current
and future networking bottlenecks.



Audience
This book was written to answer a need for a text on efficient protocol implementations. The vast
majority of networking books are on network protocols; even the implementation books are, for the
most part, detailed explanations of the protocol. While protocols form the foundation of the field, there
are just a handful of fundamental network infrastucture protocols left, such as TCP and IP. On the other
hand, there are many implementations as most companies and start-ups customize their products to
gain competitive advantage. This is exacerbated by the tendency to place TCP and IP everywhere, from
bridges to SAN switches to toasters.
                                                                                                     xix

---

## PDF page 21

xx        Preface



    Thus there are many more people implementing protocols than designing them. This is a textbook
for implementors, networking students, and networking researchers, covering ground from the art of
building a fast Web server to building a fast router and beyond.
    To do so, this book describes a collection of efficient implementation techniques; in fact, an initial
section of each chapter concludes with a Quick Reference Guide for implementors that points to the
most useful techniques for each topic. However, the book goes further and distills a fundamental method
of crafting solutions to new network bottlenecks that we call network algorithmics. This provides the
reader tools to design different implementations for specific contexts and to deal with new bottlenecks
that will undoubtedly arise in a changing world.
    Here is a detailed profile of our intended audience.
• Network Protocol Implementors: This group includes implementors of endnode networking stacks
  for large servers, PCs, and workstations and for network appliances. It also includes implementors of
  classic network interconnection devices, such as routers, bridges, switches, and gateways, as well as
  devices that monitor networks for measurement and security purposes. It also includes implementors
  of storage area networks, distributed computing infrastructures, multimedia switches and gateways,
  and other new networking devices. This book can be especially useful for implementors in start-ups
  as well as in established companies, for whom improved performance can provide an edge.
• Networking Students: Undergraduate and graduate students who have mastered the basics of network
  protocols can use this book as a text that describes how protocols should be implemented to improve
  performance, potentially an important aspect of their future jobs.
• Instructors: Instructors can use this book as a textbook for a one-semester course on network algo-
  rithmics.
• Systems Researchers: Networking and other systems researchers can use this text as a reference and
  as a stimulus for further research in improving system performance. Given that distributed operating
  systems and distributed computing infrastructures (e.g., the Grid) rely on an underlying networking
  core whose performance can be critical, this book can be useful to general systems researchers.



What this book is about
Chapter 1 provides a more detailed introduction to network algorithmics. For now, we informally define
network algorithmics as interdisciplinary systems approach to streamlining network implementations.
Network algorithmics is interdisciplinary, because it requires techniques from diverse fields such as
architecture, operating systems, hardware design, and algorithms. Network algorithmics is also a sys-
tems approach, because routers and servers are systems in which efficiencies can be gained by moving
functions in time and space between subsystems.
    In essence, this book is about three things: fundamental networking implementation bottlenecks,
general principles to address new bottlenecks, and techniques for specific bottlenecks that can be de-
rived from the general principles.
    Fundamental bottlenecks for an endnode such as a PC or workstation include data copying, con-
trol transfer, demultiplexing, timers, buffer allocation, checksums, and protocol processing. Similarly,
fundamental bottlenecks for interconnect devices such as routers and SAN switches include exact and

---

## PDF page 22

Organization of the book            xxi



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

## PDF page 23

xxii       Preface



cache efficiency. Chapter 6 shows how to reduce or avoid the overhead of transferring control between
implementation modules, such as the device driver, the kernel, and the application. Chapter 7 describes
how to efficiently manage thousands of outstanding timers, a critical issue for large servers. Chap-
ter 8 describes how to efficiently demultiplex data to receiving applications in a single step, allowing
innovations such as user-level networking. Chapter 9 describes how to implement specific functions
that often recur in specific protocol implementations, such as buffer allocation, checksums, sequence
number bookkeeping, and reassembly. An overview of Part 2 can be found in Fig. 1.1.
    Part 3 of the book, called “Playing with Routers,” shows how to build fast routers, bridges, and
gateways. It begins with three chapters that describe state lookups of increasing complexity. Chapter 10
describes exact-match lookups, which are essential for the design of bridges and ARP caches. Chap-
ter 11 describes prefix-match lookups, which are used by Internet routers to forward packets. Chapter 12
describes packet classification, a more sophisticated form of lookup required for security and quality of
service. Chapter 13 describes how to build crossbar switches, which interconnect input and output links
of devices such as routers. Finally, Chapter 14 describes packet-scheduling algorithms, which are used
to provide quality-of-service, and Chapter 15 discusses routers as distributed systems, with examples
focusing on performance and the use of design and reasoning techniques from distributed algorithms.
While this list of functions seems short, one can build a fast router by designing a fast lookup algorithm,
a fast switch, and fast packet-scheduling algorithms. Part 4, called “Endgame,” starts by speculating on
the potential need for implementing more complex tasks in the future. For example, Chapter 16 de-
scribes efficient implementation techniques for measurement primitives, while Chapter 17 describes
efficient implementation techniques for security primitives. The book ends with a short chapter, Chap-
ter 18, which reaches closure by distilling the unities that underly the many different topics in this book.
This chapter also briefly presents examples of the use of algorithmics in a canonical router (the Cisco
GSR) and a canonical server (the Flash Web server). A more detailed overview of Parts 3 and 4 of the
book can be found in Fig. 1.2.



Features
The book has the following features that readers, implementors, students, and instructors can take
advantage of.
Intuitive introduction: The introductory paragraph of each chapter in Parts 2, 3, and 4 uses an intu-
    itive, real-world analogy to motivate each bottleneck. For example, we use the analogy of making
    multiple photocopies of a document for data copying and the analogy of a flight database for prefix
    lookups.
Quick Reference Guide: For readers familiar with a topic and pressed for time, the opening section
    of each chapter concludes with a Quick Reference Guide that points to the most important imple-
    mentation ideas and the corresponding section numbers.
Chapter organization: To help orient the reader, immediately after the Quick Reference Guide in
    each chapter is a map of the entire chapter.
Summary of techniques: To emphasize the correlation between principles and techniques, at the start
    of each chapter is a table that summarizes the techniques described, together with the corresponding
    principles.

---

## PDF page 24

Why this book was written            xxiii



Consistent use of principles: After a detailed description in Chapter 3 of 15 principles, the rest of the
   book consistently uses these principles in describing specific techniques. For reference, the princi-
   ples are summarized inside the front cover. Principles are referred to consistently by number—for
   example, P9 for Principle 9. Since principle numbers are hard to remember, three aids are provided.
   Besides the inside front cover summary and the summary at the start of each chapter, the first use
   of a principle in any chapter is accompanied by an explicit statement of the principle.
Exercises: Chapter 4 of the book provides a set of real-life examples of applying the principles that
   have been enjoyed by past attendees of tutorials on network algorithmics. Every subsequent chapter
   through Chapter 17 is followed by a set of exercises. Brief solutions to these exercises can be found
   in an instructor’s manual obtainable from Elsevier.
Additional Teacher and Student Resources: Helpful ancillaries have been prepared to aid learning
   and teaching.
    • For students, resources are available here: https://www.elsevier.com/books-and-journals/book-
      companion/9780443136795.
    • For qualified professors, instructor-only teaching materials (including Lecture slides in PDF for
      most chapters) can be requested here: https://educate.elsevier.com/book/details/9780128099278.



Usage
This book can be used in many ways.
Textbook: Students and instructors can use this book as the basis of a one-semester class. A semester
    class on network algorithmics can include most of Part 1 and can sample chapters from Part 2 (e.g.,
    Chapter 5 on copying, Chapter 6 on control overhead) and from Part 3 (e.g., Chapter 11 on prefix
    lookups, Chapter 13 on switching).
Implementation guide: Implementors who care about performance may wish to read all of Part 1 and
    then sample Parts 2 and 3 according to their needs.
Reference book: Implementors and students can also use this book as a reference book in addition to
    other books on network protocols.



Why this book was written
The impetus for this book came from my academic research into efficient protocol implementation. It
also came from three networking products I worked on with colleagues: the first bridge, the Gigaswitch,
and the Procket 40 Gbps router. To prove itself against detractors, the first bridge was designed to
operate at wire speed, an idea that spread to routers and the entire industry. My experience watching
the work of Mark Kempf on the first bridge (see Chapter 10) led to a lasting interest in speeding up
networking devices.
    Next, the DEC Gigaswitch introduced me to the world of switching. Finally, the Procket router
was designed by an interdisciplinary team that included digital designers who had designed processors,
experts who had written vast amounts of the software in core routers, and some people like myself who

---

## PDF page 25


