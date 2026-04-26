# Chunk 000002

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 21–22
- From: processed/code/network-algorithmics-intro-p20-24.md

---

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

Organization of the book            xxi
