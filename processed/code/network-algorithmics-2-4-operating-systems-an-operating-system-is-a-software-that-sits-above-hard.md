# Network Algorithmics — 2.4 Operating systems An operating system is a software that sits above hardware in order to make life easier for application (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 66
- Slice: from `2.4 Operating systems An operating system is a software that sits above hardware in order to make life easier for application` up to next detected section heading

---

2.4 Operating systems
An operating system is a software that sits above hardware in order to make life easier for application
programmers. For most Internet routers, time-critical packet forwarding runs directly on the hardware
(Fig. 2.10) and is not mediated by an operating system. Less time-critical code runs on a router oper-

40        Chapter 2 Network implementation models




FIGURE 2.11
The programmer sees the illusion of an uninterrupted timeline shown above, while the real processor timeline may
switch back and forth between several processes.


ating system that is stripped down, such as Cisco’s IOS. However, to improve end-to-end performance
for, say, Web browsing, an implementor needs to understand the costs and benefits of operating systems.
    Abstractions are idealizations or illusions we invent to deal with the perversity and irregularity of
the real world. To finesse the difficulties of programming on a bare machine, operating systems offer
abstractions to application programmers. Three central difficulties of dealing with raw hardware are
dealing with interruptions, managing memory, and controlling I/O devices. To deal with these diffi-
culties, operating systems offer the abstractions of uninterrupted computation, infinite memory, and
simple I/O.
    A good abstraction increases programmer productivity but has two costs. First, the mechanism im-
plementing the abstraction has a price. For example, scheduling processes can cause overhead for a Web
server. A second, less obvious cost is that the abstraction can hide power, preventing the programmer
from making optimal use of resources. For example, operating system memory management may pre-
vent the programmer of an Internet lookup algorithm from keeping the lookup data structure in memory
in order to maximize performance. We now provide a model of the costs and underlying mechanisms of
the process (Section 2.4.1), virtual memory (Section 2.4.2), and I/O (Section 2.4.3) abstractions. More
details can be found in Tanenbaum (1992).
