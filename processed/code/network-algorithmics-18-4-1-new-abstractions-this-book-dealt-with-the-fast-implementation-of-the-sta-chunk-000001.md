# network-algorithmics-18-4-1-new-abstractions-this-book-dealt-with-the-fast-implementation-of-the-sta (chunk 000001)

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
