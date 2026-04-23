# Chunk 000004

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 23–24
- From: processed/code/network-algorithmics-intro-p20-24.md

---

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

Why this book was written            xxiii
