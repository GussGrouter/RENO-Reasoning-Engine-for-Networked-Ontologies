# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000028)

Zhao, Q., Xu, J., 2004. On the computational complexity of maintaining GPS clock in packet scheduling. In:
  Proceedings of IEEE INFOCOM.
Zhao, Q., Kumar, A., Wang, J., Xu, J., 2005. Data streaming algorithms for accurate and efficient measurement of
  traffic and flow matrices. In: Proceedings of ACM SIGMETRICS.
Zhao, Q., Ge, Z., Wang, J., Xu, J., 2006a. Robust traffic matrix estimation with imperfect information: making use
  of multiple data sources. In: Proceedings of ACM SIGMETRICS.
Zhao, Q., Xu, J., Liu, Z., 2006b. Design of a novel statistics counter architecture with optimal space and time
  efficiency. In: Proceedings of ACM SIGMETRICS.
Zhao, H. (Chuck), Wang, H., Lin, B., Xu, J. (Jim), 2009. Design and performance analysis of a DRAM-based
  statistics counter array architecture. In: Proceedings of the 5th ACM/IEEE Symposium on Architectures for
  Networking and Communications Systems, ANCS’09. ACM, New York, NY, pp. 84–93.
Zhao, H. (Chuck), Lall, A., Ogihara, M., Xu, J., 2010. Global iceberg detection over distributed data streams. In:
  Proceedings of IEEE ICDE.
Zhao, S., Wang, R., Zhou, J., Ong, J., Mogul, J.C., Vahdat, A., 2019. Minimal rewiring: efficient live expansion for
  clos data center networks. In: 16th USENIX Symposium on Networked Systems Design and Implementation
  (NSDI 19). USENIX Association, Boston, MA, pp. 221–234.

This page intentionally left blank

Index

A                                                   Banyan, 540
Acknowledgments (ack), withholding, 99–101          Barrel shifters, 24
Active messages, 168                                Batch allocator, 214, 215
Adaptor memory, 115–117                             Batching, 59, 173
Address lookup, 252                                 Benes networks, 370–375
Address Resolution Protocol (ARP), 38               Berkeley packet filter (BPF), 152, 199–201
Addresses, Internet, 252                            BGP (Border Gateway Protocol), 18, 443, 444
Admission control, 392                              Binary search
Afterburner approach, 116, 117                        of long identifiers, 103–105
Aggregation                                           on prefix lengths, 278–280
                                                      on ranges, 275–277
  edge, 425, 426
                                                      on ranges with initial lookup table, 277, 278
  random, 425
                                                      pipelining, 244, 245
  threshold, 464–466
                                                    Binary trees, balanced, 29
Aho–Corasick algorithm, 490–493
                                                    Binomial bucketing, 95
Algorithms versus algorithmics, 55, 56              Bit slicing, 375, 376
American National Standards Institute (ANSI), 128   Bit vector linear search, 316–318
Anomaly intrusion detection, 489                    Bit-by-bit round-robin, 395
Apache Web server, 155                              Bitmap, tree, 271–274
API                                                 Blockade state, 393
  speeding up select() by changing, 164, 165        Bloom filters, 501, 502
  speeding up select() without changing, 163, 164   Bottlenecks, 3
Appletalk, 38, 237                                    endnode, 4, 5
Application code, 146                                 router, 5–7
Application device channel (ADC), 168               Boyer–Moore algorithm, 493–495
  buffer validation of, 76–78                       BPF (Berkeley packet filter), 152, 199–201
Architecture                                        Bridges/bridging, 82, 83
  endnode, 33–35                                      defined, 235
  router, 35–39                                       Ethernets, 236–238
  virtual interface, 169                              scaling lookups to higher speeds, 242–246
Asynchronous transfer mode (ATM)                      wire speed forwarding, 238–242
  flow control, 78, 79                              BSD UNIX, 41, 42, 173
  video conferencing via, 105–107                     callouts and timers, 189, 190
                                                    Bucket sorting, 80, 95, 96
                                                    Buddy system, 213, 214
B                                                   Buffer(s)
Backtracking, 14, 307, 308                            aggregates, 132
Baker, Fred, 241                                      allocation, 5, 212–215
Bandwidth, 28                                         dynamic buffer limiting, 216
  guarantees, 393–399                                 fast, 119–123
  reduce collection, 469, 470                         management, 212, 217
  scaling, 5                                          overflow, 8
Banks, 28                                             sharing, 215–217, 432
                                                                                                      559

560        Index
