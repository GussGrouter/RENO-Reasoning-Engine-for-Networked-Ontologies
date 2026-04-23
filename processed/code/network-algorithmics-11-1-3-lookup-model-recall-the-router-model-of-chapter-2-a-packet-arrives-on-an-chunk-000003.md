# network-algorithmics-11-1-3-lookup-model-recall-the-router-model-of-chapter-2-a-packet-arrives-on-an (chunk 000003)

The seventh observation comes from Chapter 2. While standard (DRAM) memory is cheap, DRAM
access times are currently around 20–40 nanoseconds, and so higher-speed memory (e.g., off- or on-
chip SRAM, 1–5 nanoseconds) may be needed at higher speeds. While DRAM memory is essentially
unlimited, SRAM and on-chip memory are limited by expense or unavailability. Thus a third metric is
memory usage, where memory can be expensive fast memory (cache in software, SRAM in hardware)
as well as cheaper, slow memory (e.g., DRAM, SDRAM).
    Note that a lookup scheme that does not do incremental updates will require two copies of the
lookup database so that search can proceed in one copy while lookups proceed on the other copy. Thus
it may be worth doing incremental updates simply to reduce high-speed memory by a factor of 2!
    The eighth observation concerns prefix lengths. IPv6 requires 128-bit prefixes. Multicast lookups
require 64-bit lookups because the full group address and a source address can be concatenated to make
a 64-bit prefix. However, the full deployment of both IPv6 and multicast is still proceeding. Thus at the
time of writing, it is important to be able to support both 32-bit and 128-bit IP lookups.
    In summary, the interesting metrics, in order of importance, are lookup speed, memory, and update
time. As a concrete example, a good on-chip design using 16 Mbits of on-chip memory may support
any set of 1,000,000 prefixes, do a lookup in 8 nanoseconds to provide wire speed forwarding at terabit
speeds, and allow prefix updates in 1 millisecond.
    The following notations is used consistently in reporting the theoretical performance of IP lookup
algorithms. N denotes the number of prefixes (e.g., 900,000 for large databases in 2022), and W denotes
the length of an address (e.g., 32 for IPv4).
    Finally, two additional observations can be exploited to optimize the expected case.
O1: Almost all prefixes are 24 bits or less, with the majority being 24-bit prefixes and the next largest
    spike being at 16 bits. Some vendors use this to show worst-case lookup times only for 24-bit
    prefixes; however, the future may lead to databases with a large number of host routes (32-bit
    addresses) and integration of ARP caches.
O2: It is fairly rare to have prefixes that are prefixes of other prefixes, such as the prefixes 00* and
    0001*. In fact, the maximum number of prefixes of a given prefix in current databases is seven.
   While the ideal is a scheme that meets worst-case lookup time requirements, it is desirable to have
schemes that also utilize these observations to improve average storage performance.
