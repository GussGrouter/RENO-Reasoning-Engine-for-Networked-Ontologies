# network-algorithmics-1-1-2-router-bottlenecks-though-we-concentrate-on-internet-routers-almost-all (chunk 000002)

Many routers today offer what is sometimes called service differentiation, where different packets
can be treated differently in order to provide service and security guarantees. Unfortunately, this re-
quires an even more complex form of lookup called packet classification, in which the lookup is based
on the destination, source, and even the services that a packet is providing. This challenging issue is
tackled in Chapter 12.
    Next, all networking devices can be abstractly considered as switches that shunt packets coming in
from a set of input links to a set of output links. Thus a fundamental issue is that of building a high-
speed switch. This is hard, especially in the face of the growing gap between optical and electronic
speeds. The standard solution is to use parallelism via a crossbar switch. Unfortunately, it is nontrivial
to schedule a crossbar at high speeds, and parallelism is limited by a phenomenon known as head-of-
line blocking. Worse, population scaling and optical multiplexing are forcing switch vendors to build
switches with a large number of ports (e.g., 256), which exacerbates these other problems. Solutions to
these problems are described in Chapter 13.
    While the previous bottlenecks are caused by scaling, the next bottleneck is caused by the need for
new services. The issue of providing performance guarantees at high speeds is treated in Chapter 14,
where the issue of implementing so-called QoS (quality of service) mechanisms is studied. Chapter 15
briefly surveys another bottleneck that is becoming an increasing problem: the issue of bandwidth
within a router. It describes sample techniques, such as striping across internal buses and chip-to-chip
links.

1.2 The techniques: network algorithmics                      7

The final sections of the book take a brief look at emerging services that must, we believe, be part of
a well-engineered Internet of the future. First, routers of the future must build in support for measure-
ment, because measurement is the key to engineering networks to provide guarantees. While routers
today provide some support for measurement in terms of counters and NetFlow records, Chapter 16
also considers more innovative measurement mechanisms that may be implemented in the future.
    Chapter 17 describes security support, some of which is already being built into routers. Given the
increased sophistication, virulence, and rate of network attacks, we believe that implementing security
features in networking devices (whether routers or dedicated intrusion prevention/detection devices)
will be essential. Further, unless the security device can keep up with high-speed links, the device may
miss vital information required to spot an attack.
