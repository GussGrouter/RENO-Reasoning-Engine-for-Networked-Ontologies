# Network Algorithmics — 18.4.1 New abstractions This book dealt with the fast implementation of the standard networking abstractions: TCP sockets at (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 552
- Slice: from `18.4.1 New abstractions This book dealt with the fast implementation of the standard networking abstractions: TCP sockets at` up to next detected section heading

---

18.4.1 New abstractions
This book dealt with the fast implementation of the standard networking abstractions: TCP sockets at
endnodes and IP routing at routers. However, new abstractions are constantly being invented to increase
user productivity. While these abstractions make life easier for users, unoptimized implementations of
these abstractions can exact a severe performance penalty. But this only creates new opportunities for
network algorithmics. Here are some examples of such abstractions.
• TCP offload engines: While the book has concentrated on software TCP implementations, move-
  ments such as iSCSI have made hardware TCP offload engines more interesting. Doing TCP in
  hardware and handling worst-case performance at 10 Gbps and even 40 Gbps is very challenging.
  For example, to do complete offload, the chip must even handle out-of-order packets and packet frag-
  ments (see Chapter 9) without appreciable slowdown. TCP Offload has become a reality at speeds
  like 1 Gbps since the first edition of the book. For example, in Windows Server 2008, TCP Chimney
  Offload 2022 can relegate the processing of a TCP/IP connection to a network adapter (such as from
  Broadcome) that includes TCP/IP offload processing.
• HTML and Web server processing: There have been a number of papers trying to improve Web
  server performance that can be considered an application of endnode algorithmics. For example,
  persistent HTTP (Mogul, 1995) can be considered an application of P1 to the problem of connection

526        Chapter 18 Conclusions



    overhead. A more speculative approach to reduce DNS lookup times in Web accesses by passing
    hints (P10) is described in Chandranmenon and Varghese (2001).
•   Web services: The notion of Web services, by which a Web page is used to provide a service, is get-
    ting increasingly popular. There are a number of protocols that underly Web services, and standard
    implementations of these services can be slow.
•   CORBA: The common object request broker architecture is popular but quite slow. Gokhale and
    Schmidt (1998) apply to the problem four of the principles described in this book (eliminating waste,
    P1, optimizing the expected case, P11, passing information between layers, P9, and exploiting lo-
    cality for good cache behavior, P4a). They show that such techniques from endnode algorithmics
    can improve the performance of the SunSoft Inter-Orb protocol by a factor of 2–4.5, depending on
    the data type. Similar optimizations should be possible in hardware.
•   SSL and other encryption standards: Many Web servers use the secure socket layer (SSL) for secure
    transactions. Software implementations of SSL are quite slow.
•   XML processing: XML is rapidly becoming the lingua franca of the Web. Parsing and converting
    from XML to HTML can be a bottleneck.
•   Measurement and security abstractions: Currently, SNMP and NetFlow allow very primitive mea-
    surement abstractions. The abstraction level can be raised only by a tool that integrates all the raw
    measurement data. Perhaps in the future routers will have to implement more sophisticated abstrac-
    tions to help in measurement and security analysis.
•   Sensor networks: A sensor network may wish to calculate new abstractions to solve such specific
    problems as finding high concentrations of pollutants and ascertaining the direction of a forest fire.
    If history is any guide, every time an existing bottleneck becomes well studied, a new abstrac-
tion appears with a new bottleneck. Thus after lookups became well understood, packet classification
emerged. After classification came TCP offload; and now SSL and XML are clearly important. Many
pundits believe that wire speed security solutions (as implemented in a router or an intrusion detec-
tion system) will be required by the year 2006. Thus it seems clear that future abstractions will keep
presenting new challenges to network algorithmics.
