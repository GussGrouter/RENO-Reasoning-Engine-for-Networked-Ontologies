# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000033)

Multicast, 337, 340, 351                              passing labels, 303
Multichassis routers, 363, 364, 366–370               reasons for, 296–298
Multiplexers, 24                                      requirements and metrics, 301
Multithreading, 39                                    role of, 295
                                                      routers, 295
N                                                     Tuple Space Search (TSS), 301
Net-dispatch, 150                                     two dimensional, 304–310, 313–315
NetFlow, 468, 469                                   Packet filters
Network address translation (NAT), 252, 297           Berkeley (BPF), 152, 199–201
Network algorithmics                                  CMU Stanford (CSPF), 152, 198, 199, 208
  algorithms versus, 55, 56                           dynamic, 205–208
  characteristics of, 13–15                         Packet steering, 173
  defined, 14, 519–523                              Packetized generalized processor sharing (PGPS), 400
  future, 525–527                                   Packets, 18
  real products and, 524, 525                         filtering in routers, 87–90
  techniques, 7–15                                    flow, 385
Network processors, 36, 38, 39                        header validation and checksums, 37
Networking code, avoiding scheduling overhead in,     logs, 453, 468
           149–153                                    repeater, 237, 238
Node compression, tries and, 85–87                    scheduling, 383–427
  1D torus, 376                                     Page mode, 28, 240
                                                    Page remapping, 119–123
                                                    Pages, 43
O
                                                    Parallel iterative matching (PIM), 344–347
Offload Mechanisms, 173
                                                    Parallelism, hardware, 244
Operating systems
                                                    Pareto optimality, 215
  system calls and simple, 44
                                                    Path MTU, 228
  uninterrupted computation, 40–42
                                                    PathFinder, 152, 201–205, 303
  virtual memory, 42, 43                            Patricia trie, 14, 261
OSPF, 18, 37, 79                                    pbufs, 213
Output queuing, 342, 343                            Per-prefix counters, 474
Output scheduling, 37                               Perfect hashing, 243
                                                    Performance, improving, 431, 432, 435, 436, 439, 442
P                                                   Performance measures, 21
P4 Language                                           for timers, 181
  model, functionality, applications, 287, 288        select() and server performance problem, 159, 160
Packet classification, 6, 37, 197, 295              Perlman, Radia, 241
  caching, 302                                      PerTickBookkeeping, 181, 182
  content-addressable memory, 304                   Physical reception, 435
  cross-producting, 318–320                         Piggybacking, 101
  cross-producting, equivalenced, 320–323           Ping, 475
  decision trees, 323–326                           Pipelining, 29, 30, 244, 245
  demultiplexing, 303                               Polling, 173, 175
  divide-and-conquer, 315–323                       Population scaling, 5
  extended grid of tries, 313                       Prefix-match lookups, 5, 36
  geometric view, 311, 312                            binary search, on ranges, 275–277
  grid of tries, 308–310                              binary search, on ranges, with initial lookup table,
  linear search, 301                                             277, 278
  linear search, bit vector, 316–318                  binary search, prefix lengths, 278–280

Index        565

flow switching, 256, 257                             R
  linear search, prefix lengths, 280–283               Random early detection (RED), 386, 388
  memory allocation, 283–285                           Randomization
  model, 252–254                                         avoiding, 347–352
  model, lookup-chip, 285, 286                           memory scaling using, 377, 378
  model, programmable processors, P4, 286, 287         Rate sharing, 432
  multi-protocol label switching, 38, 256–258, 303     Rational, Quantify, 21
  nonalgorithmic techniques for, 258, 259              Reading large databases, incremental, 101–103
  notation, 250, 251                                   Rearrangeably nonblocking, 368
  threaded indices and tag switching, 14, 255–257      Reassembly, 20, 227–230
  tree bitmaps, 271–274                                Receive Flow Steering, 173
                                                       Receive Packet Steering, 173
  tries, level-compressed, 267, 268
                                                       Receiver livelock, 41, 42
  tries, Lulea-compressed, 268–271
                                                         avoiding, 173, 174
  tries, multibit, 262–267
                                                       Reception
  tries, unibit, 259, 262
                                                         logical, 435
  variable-length, reasons for, 252
                                                         physical, 435
Priorities, 348, 349, 351, 391                         Recursive flow classification (RFC), 296, 320, 323,
Priority encoder (PE), 24                                          329
Probabilistic counting, 467                            Redirects, 38
Probabilistic marking, 497–499                         Reentrant, 152
Programmable logic array (PLA), 535                    Registered memory, 169
Programmable priority encoder (PPE), 24–26, 351, 359   Registers, 27, 536
Protocol control block (PCB), 224–226                  Reliability, 432–434, 436–439, 443
Protocol Engines, Inc., 224                            Remote direct memory access (RDMA), 112, 126–130
Protocol processing                                    Repeaters
  buffer management, 212–217                             filtering, 238
  checksums and cyclic redundancy checks, 217–223        packet, 237
  generic, 224–227                                     Resemblance, 496
  reassembly, 227–230                                  Reservation protocols, 392, 393
Protocols, 18–20, 37, 38                               Resource Reservation Protocol (RSVP), 393
  reservation, 392                                     Resources, identifying, 94–96
Pushout, 216                                           Restructuring
                                                         OS, 171, 172
                                                       RIP, 18, 37
Q
                                                       Round-robin
Quality of service (QOS), 22, 383, 392
                                                         deficit (bit-by-bit), 395–398
  reasons for, 385, 386
                                                         slice-by-slice, 393–395
Queue-Proportional Sampling (QPS), 332                 Routers, 3, 5–7, 429, see also Distributed systems,
  algorithm, 357                                                   routers as
  behavior, 357                                          architecture, 35–39
  data structure, 356–358                                fragmentation, redirects and ARPs, 38, 39
  implementation, 357                                    history of, 335, 336
  strategy, 356                                          lookup, 36, 37
Queuing, 37                                              multichassis, 363, 364, 366–370
  class-based, 398, 399                                  packet classification, 295
  multiple outbound, 391, 392                            packet filtering in, 87–90
  output, 342, 343                                       pin-count for buffers, 31, 32
  scalable fair, 424–426                                 processing, 37, 38
