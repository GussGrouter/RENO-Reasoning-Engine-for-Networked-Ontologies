# network-algorithmics-5-3-2-modern-day-incarnations-of-rdma (chunk 000002)

Infiniband
Infiniband starts with the observation that the internal I/O bus used within many workstations and PCs,
the PCI bus, is showing its age and needs replacement. With a maximum bandwidth of 533 MB/sec, the
PCI bus is being overwhelmed by modern high-speed peripherals, such as Gigabit Ethernet interface
cards. While there are some temporary alternatives, such as the PCI-X bus, the internal computer inter-
connect needs to scale in the same way as the external Internet has scaled from, say, 10-Mbit Ethernet
to Gigabit Ethernet.
    Also, observe that there are three separate networking technologies within a computer: the network
interface (e.g., Ethernet), the disk interface (e.g., SCSI over Fibre Channel), and the PCI bus. Occam’s
razor suggests substituting these three with one network technology. Accordingly, Compaq, Dell, HP,
IBM, and Sun banded together to form the Infiniband Trade Association.
    The Infiniband specifications use many of the ideas in Fibre Channel’s underlying network technol-
ogy. The interconnect is also based on switches and point-to-point links. Infiniband has a few additional
twists. It uses the proposal for 128-bit IP addresses in the next-generation Internet as a basis for ad-
dressing. It allows individual physical links to be virtualized into separate virtual links called lanes.
It has features for quality of service and even multicast. Once again, RDMA is the key technology to
avoid copies.
    While Infiniband has not enjoyed the spurt in popularity of Ethernet based solutions described next
or even that of Fibre Channel in Storage Area Networks, it is still widely used in supercomputing instal-
lations for high performance computing (SHARP, 2019). It is also used for speeding up large machine
learning workloads using abstractions for in-network computing called SHARP that we describe in
Section 5.5. For instance, it is used in two of the world’s largest supercomputers in Oakridge and Los
Alamos, with close to 10,000 Infiniband nodes each (SHARP, 2019).

iSCSI via iWarp and RoCE
Given that IP has invaded various other networking spaces, such as voice, TV, and radio, a natural
consequence is to invade the storage space. This, the argument goes, should drive down prices (while
also opening up new markets for network vendors). Further, Fibre Channel and Infiniband are being
extended to connect remote data centers over the Internet. This involves using transport protocols that
are not necessarily compatible with TCP in terms of reacting to congestion. Why not just adapt TCP
for this purpose instead of trying to modify these other protocols to be TCP friendly?
    For the purposes of this chapter, the most interesting thing about iSCSI is the way it must emulate
RDMA over standard IP protocols. In particular recall that in all RDMA implementations, the host

130      Chapter 5 Copying data
