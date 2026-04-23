# network-algorithmics-15-3-2-rescuing-reliability (chunk 000003)

15.4 Asynchronous updates                441

Further, if it is known that queues do not behave completely adversarially, the head cache size can be
reduced further.
    The distributed memory algorithms described in this section have had a large impact. They were first
commercialized in a startup called Nemo founded by Iyer and McKeown. After Nemo was acquired by
Cisco, it began to considerably impact Cisco routers. By some estimates in Iyer’s thesis Sundar (2008)
distributed memory within Cisco alone is used by several million chips per year in over 7 product lines,
saving hundreds of millions of dollars per year by replacing SRAM with cheap off-chip DRAM, while
allowing queue sizes in the thousands. While the more complex algorithms were used rarely, the simple
most deficited queue algorithm was used in the vast majority of Cisco head cache implementations. For
the tail cache, the simple dynamically allocated cache of size Qb was universally used.
    Besides the memory savings, other advantages include reduced power, reduced pins on ASICs (to
deal with multiple memories), and better utiilization. The better utilization comes from the batching
into blocks of b. A surprising side effect is to eliminate the thorny problem of what happens when
65 byte packets are sent when the internal SRAM cell size is 64 bytes. Such memory fragmentation
becomes less of an issue when a stream of 65 byte packets are batched in a tail cache of size b = 640
bytes (say). A second subtle advantage is that these provably worst case queues eliminate packet drops:
this is crucial for example in the storage market (Sundar, 2008), as well as other applications whose
QoS requirements require strict bounded latency.
