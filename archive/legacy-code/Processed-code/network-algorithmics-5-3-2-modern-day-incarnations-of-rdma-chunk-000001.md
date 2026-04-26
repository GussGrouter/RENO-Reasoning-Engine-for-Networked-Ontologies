# network-algorithmics-5-3-2-modern-day-incarnations-of-rdma (chunk 000001)

# Network Algorithmics — 5.3.2 Modern-day incarnations of RDMA (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 155
- Slice: from `5.3.2 Modern-day incarnations of RDMA` up to next detected section heading

---

5.3.2 Modern-day incarnations of RDMA
VAX Clusters introduced a very early storage area network. Storage area networks (SANs) are back-
end networks that connect many computers to shared storage, in terms of network-attached disks. There
are several successors to VAX Clusters that provide SAN technology today. These range from the
venerable Fiber Channel (Benner, 1995) technology to modern upstarts such as Infiniband (Infiniband
Trade Association, 2001) and iSCSI (Satran et al., 2001).

Fiber channel
In 1988 the American National Standards Institute (ANSI) Task Group X3T11 began work on a stan-
dard called Fibre Channel (Benner, 1995). One of the goals of Fibre Channel was to take the standard
SCSI (small computer system interface) between a workstation and a local disk and extend it over larger
distances. Thus in many Fibre Channel installations, SCSI is still used as the protocol that runs over
Fiber Channel.
    Fibre Channel goes further than VAX Clusters in the underlying network, using modern network
technology such as point-to-point fiber links connected with switches. This allows speeds of up to 64
Gbps and allows a larger distance span than in the Vax Cluster network. Switches can even be remotely
connected, allowing a trading firm to have backup storage of all trades at a remote site. The use of
switches requires attention to such issues as credit flow control, which is done very carefully to avoid
dropping packets where possible to maintain the illusion of a lossless computer bus over the network.
    Fibre Channel also makes slightly more concession to security than VAX Clusters. In VAX Clusters
any device with the right name can overwrite the memory of any other device. Fiber Channel allows
the network to be virtualized into zones. Nodes in a zone cannot access the memory of nodes in other
zones. Some recent products go even further and propose techniques based on authentication.

5.3 Avoiding copying using remote DMA                129

However, other than these differences in the underlying technology, the underlying ideas are the
same. RDMA via named buffers is still a key enabling idea. While Fibre Channel has had much recent
competition from Ethernet based RDMA methods such as RoCE (Guo et al., 2016) (see below), it
has still been the mainstay of storage area networks (SANs) for two decades and shows no signs of
disappearing.
    One reason for its continued popularity (The State of Fibre Channel, 2022) may be the popularity of
solid state disks or NVM (Non Volatile Memory) especially over the PCI Express bus (NVMe). Fibre
Channel latencies are particularly low. Thus despite the potential cost advantages of Ethernet solutions,
the performance of Fibre Channel may explain its continued use in SANs.
