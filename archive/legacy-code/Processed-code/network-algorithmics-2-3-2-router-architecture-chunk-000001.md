# network-algorithmics-2-3-2-router-architecture (chunk 000001)

# Network Algorithmics — router architecture (2.3.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 62 -l 71 -layout
- Slice: from `2.3.2 Router architecture` up to (excluding) `2.4 Operating systems`

---

2.3.2 Router architecture
A router model that covers both high-end routers (such as Juniper’s M-series routers) and low-end
routers (such as the Cisco Catalyst) is shown in Fig. 2.10. Basically, a router is a box with a set of input
links, shown on the left, and a set of output links, shown on the right; the task of the router is to switch
a packet from an input link to the appropriate output link based on the destination address in the packet.
While the input and output links are shown separately, the two links in each direction between two
routers are often packaged together. We review three main bottlenecks in a router: lookup, switching,
and output queuing.

---

## PDF page 63

36        Chapter 2 Network implementation models

FIGURE 2.10
A model of a router labeled with the three main bottlenecks in the forwarding path: address lookup (B1), switching
(B2), and output scheduling (B3).

Lookup
A packet arrives on, say, the left link, input link i. Every packet carries a 32-bit Internet Protocol (IP)
address.10 Assume that the first six bits of the destination address of a sample packet are 100100. A
processor in the router inspects the destination address to determine where to forward the packet.
    The processor consults a forwarding table to determine the output link for the packet. The forward-
ing table is sometimes called a FIB, for forwarding information base. The FIB contains a set of prefixes
with corresponding output links. The reason for prefixes will be explained in Chapter 11; for now, think
of prefixes as variable-length “area codes” that greatly reduce the FIB size. A prefix like 01*, where the
* denotes the usual “don’t care” symbol, matches IP addresses that start with 01. Assume that prefix
100* has associated output link 6, while prefix 1* has output link 2. Thus our sample packet, whose
destination address starts with 100100, matches both prefixes 100* and 1*. The disambiguating rule
that IP routers use is to match an address to the longest matching prefix. Assuming no longer matching
prefixes, our sample packet should be forwarded to output link 6.
    The processor that does the lookup and basic packet processing can be either shared or dedicated
and can be either a general processor or a special-purpose chip. Early router designs used a shared
processor (or processors), but this proved to be a bottleneck. Later designs, including Cisco’s GSR
family, use a dedicated processor per input link interface. The earliest designs used a standard CPU
processor, but many of the fastest routers today, such as Juniper’s M-160, use a dedicated chip (ASIC)
with some degree of programmability. There has been a backlash to this trend toward ASICs, however,
with customers asking routers to perform new functions, such as Web load balancing. Thus some new
routers use network processors (see Example 7), which are general-purpose processors optimized for
networking.

10 Recall that while most users deal with domain names, these names are translated to an IP address by a directory service,
called DNS, before packets are sent.

---

## PDF page 64

2.3 Network device architectures                         37

Algorithms for prefix lookups are described in Chapter 11. Many routers today also offer a more
complex lookup called packet classification (Chapter 12), where the lookup takes as input the destina-
tion address as well as source address and TCP ports.
