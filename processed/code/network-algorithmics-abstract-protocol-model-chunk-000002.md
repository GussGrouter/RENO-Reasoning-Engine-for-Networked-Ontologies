# Chunk 000002

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 46–47
- From: processed/code/network-algorithmics-abstract-protocol-model-p45-47.md

---

This book is devoted to protocol implementations. Besides TCP and IP, this book will consider other
protocols, such as HTTP. Thus, it is worth abstracting out the generic and time-consuming functions
that a protocol state machine performs based on our TCP and routing examples. Such a model, shown
in Fig. 2.2, will guide us through this book.
    First, at the bottom of Fig. 2.2, a protocol state machine must receive and send data packets. This
involves data manipulations, or operations that must read or write every byte in a packet. For instance,
a TCP must copy received data to application buffers, while a router has to switch packets from input
links to output links. The TCP header also specifies a checksum that must be computed over all the data
bytes. Data copying also requires the allocation of resources such as buffers.
    Second, at the top of Fig. 2.2, the state machine must demultiplex data to one of many clients. In
some cases, the client programs must be activated, requiring potentially expensive control transfer. For
instance, when a receiving TCP receives a Web page, it has to demultiplex the data to the Web browser
application using the port number fields and may have to wake up the process running the browser.

---

20       Chapter 2 Network implementation models

Fig. 2.2 also depicts several generic functions shared by many protocols. First, protocols have a
crucial state that must be looked up at high speeds and sometimes manipulated. For instance, a received
TCP packet causes TCP to look up a table of connection state, while a received IP packet causes IP
to look up a forwarding table. Second, protocols need to efficiently set timers, for example, to con-
trol retransmission in TCP. Third, if a protocol module is handling several different clients, it needs
to schedule these clients efficiently. For instance, TCP must schedule the processing of different con-
nections, while a router must make sure that unruly conversations between some pair of computers do
not lock out other conversations. Many protocols also allow large pieces of data to be fragmented into
smaller pieces that need reassembly.
    One of the major theses of this book is that though such generic functions are often expensive, their
cost can be mitigated with the right techniques. Thus each generic protocol function is worth studying in
isolation. Therefore after Part 1 of this book, the remaining chapters address specific protocol functions
