# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000001)

# Network Algorithmics — 18.5 The inner life of a networking device (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 555
- Slice: from `18.5 The inner life of a networking device` up to next detected section heading

---

18.5 The inner life of a networking device
We have tried to summarize in this chapter the major themes of this book in terms of the techniques
described and the principles used. We have also tried to argue that network algorithmics is used in
real products and is likely to find further application in the future because of new abstractions, new
connecting disciplines, and new requirements. While the specific techniques and problems may change,
we hope the principles involved remain useful.
    Besides the fact that network algorithmics is useful in building better and faster network devices,
we hope this book makes the case that network algorithmics is also intellectually stimulating. While it
may lack the depth of hard problems in theoretical computer science or physics, perhaps what can be
most stimulating is the breadth, in terms of the disciplines it encompasses.
    An endnode, for instance, may appear as a simple processing state machine at the highest level of
abstraction. A more detailed inspection would see a Web request packet arriving at a server interface,
the interrupt firing, and the protocol code being scheduled via a software interrupt. Even within the
protocol code, each line of code has to be fetched, hopefully from the I-cache, and each data item has
to go through the VM system (via the TLB hopefully) and the data cache. Finally, the application must
get involved via a returned system call and a process-scheduling operation. The request may trigger file
system activity and disk activity.
    A router similarly has an interesting inner life. Reflecting the macrocosmos of the Internet outside
the router is a microcosmos within the router consisting of major subsystems, such as line cards and the
switch fabric, together with striping and flow control across chip-to-chip links.
    Network algorithmics seeks to understand these hidden subsystems of the Internet to make the In-
ternet faster. This book is a first attempt to begin understanding, in Feynman’s phrase, this “tremendous
world of interconnected hierarchies” within routers and endnodes. In furthering this process of under-
standing and streamlining these hierarchies, there are still home runs to be hit and touchdowns to be
scored as the game against networking bottlenecks continues to be played.

APPENDIX

Detailed models
                                                                                           A
This appendix contains further models and information that can be useful for some readers of this
book. For example, the protocols section may be useful for hardware designers who wish to work
in networking but need a quick self-contained overview of protocols such as TCP and IP to orient
themselves. On the other hand, the hardware section provides insights that may be useful for software
designers without requiring a great deal of reading. The switch section provides some more details
about switching theory.

A.1 TCP and IP
To be self-contained, Section A.1.1 provides a very brief sketch of how transmission control protocol
(TCP) operates, and Section A.1.2 briefly describes how IP routing operates.
