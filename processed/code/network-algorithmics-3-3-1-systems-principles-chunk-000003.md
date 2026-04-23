# network-algorithmics-3-3-1-systems-principles (chunk 000003)

• P3a: Trade Certainty for Time. Systems designers can fool themselves into believing that their
  systems offer deterministic guarantees, when in fact we all depend on probabilities. For example,
  quantum mechanics tells us there is some probability that the atoms in your body will rearrange
  themselves to form a hockey puck, but this is clearly improbable.2 This opens the door to consider
  randomized strategies when deterministic algorithms are too slow.
  In systems, randomization is used by millions of Ethernets worldwide to sort out packet-sending
  instants after collisions occur. A simple networking example of randomization is Cisco’s NetFlow
  traffic measurement software: If a router does not have enough processing power to count all arriving
  packets, it can count random samples and still be able to statistically identify large flows. A second
  networking example is stochastic fair queuing (Chapter 14), where, rather than keep track exactly
  of the networking conversations going through a router, conversations are tracked probabilistically
  using hashing.
• P3b: Trade Accuracy for Time. Similarly, numerical analysis cures us of the illusion that comput-
  ers are perfectly accurate. Thus it can pay to relax accuracy requirements for speed. In systems,
  many image compression techniques, such as MPEG, rely on lossy compression using interpolation.
  Chapter 1 used approximate thresholds to replace divides by shifts. In networking, some packet-
  scheduling algorithms at routers (Chapter 14) require sorting packets by their departure deadlines;
  some proposals to reduce sorting overhead at high speeds suggest approximate sorting, which can
  slightly reduce quality-of-service bounds but reduce processing.
• P3c: Shift Computation in Space. Notice that all the examples given for this principle relaxed re-
  quirements: Sampling may miss some packets, and the transferred image may not be identical to the
  original image. However, other parts of the system (e.g., Subsystem 2 in Fig. 3.8) have to adapt to
  these looser requirements. Thus we prefer to call the general idea of moving computation from one
  subsystem to another (“robbing Peter to pay Paul”) shifting computation in space. In networking, for
  example, the need for routers to fragment packets has recently been avoided by having end systems
  calculate a packet size that will pass all routers.

P4: Leverage off system components
A black-box view of system design is to decompose the system into subsystems and then to design
each subsystem in isolation. While this top-down approach has a pleasing modularity, in practice
performance-critical components are often constructed partially bottom-up. For example, algorithms
are designed to fit the features offered by the hardware. Here are some techniques that fall under this
principle.
• P4a: Exploit Locality. Chapter 2 showed that memory hardware offers efficiencies if related data
  is laid out contiguously, e.g., same sector for disks, or same DRAM page for DRAMs. Disk-search
  algorithms exploit this fact by using search trees of high radix, such as B-trees. IP-lookup algorithms
  (Chapter 11) use the same trick to reduce lookup times by placing several keys in a wide word, as
  did the example in Chapter 1.
• P4b: Trade Memory for Speed. The obvious technique is to use more memory, such as lookup tables,
  to save processing time. A less obvious technique is to compress a data structure to make it more
  likely to fit into cache, because cache accesses are cheaper than memory accesses; in this case,

2 Quote due to Tony Lauck.

---

## PDF page 88

3.3 Fifteen implementation principles—categorization and description                                            61
