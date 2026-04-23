# network-algorithmics-6-5-3-single-root-i-o-virtualization-sr-iov (chunk 000001)

# Network Algorithmics — 6.5.3 Single Root I/O Virtualization (SR-IOV) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 197
- Slice: from `6.5.3 Single Root I/O Virtualization (SR-IOV)` up to next detected section heading

---

6.5.3 Single Root I/O Virtualization (SR-IOV)
As we said in the introduction to this chapter, the world has changed. Virtualization has become per-
vasive to improve physical server utilization and for other reasons. Thus many virtual machines (VMs)
are safely multiplexed together in a single physical machine by the addition of another operating system
layer called a hypervisor. To allow networking between virtual machines on the same physical server,
the hypervisor must include a virtual switch. Unfortunately, the virtual switch adds another layer of
overhead when VMs send networking packets to other VMs in other physical servers.
    Just as kernel bypass mechanisms like DPDK bypass the kernel, the idea in Single Root I/O Vir-
tualization (SR-IOV) is to add hardware protection mechanisms in the network interface to bypass the
virtual switch and hypervisor. This is done by a hardware IOMMU (I/O Memory Mapping Unit) that
helps the NIC translate device virtual addreses to physical addresses just as a MMU helps the CPU to
do so for other virtual addresses. By having the hypervisor initially create these mappings for each VM,
each VM gets protected access to the NIC without hypervisor mediation once the mappings have been
created. This creates what SR-IOV calls a “virtual function” in which each VM sees a virtual NIC all to

6.6 Radical Restructuring of Operating Systems                 171

itself, in addition to the “physical function” which is the actual SR-IOV capable NIC. The term “Single
Root” is confusing but refers to the the fact that in SR-IOV the PCI Express device is shared within a
single computer.
    If most communication is between VMs in the same physical server, DPDK should suffice; but if
communication is between VMs in different servers, SR-IOV can improve performance by bypassing
the hypervisor.
    Despite its origins in the world of virtualization, SR-IOV is part of the PCIe standard and so is much
more general than it may first appear. It does not require a hypervisor or even VMs to be used. This
is exploited in some proposals such as Arrakis (Peter et al., 2015) to generalize the operating system
to allow more streamlined I/O processing for other functions such as storage, and even in High Per-
formance Computing. Arrakis refactors the classical operating system kernel to be merely the control
plane, avoiding the need for kernels to be involved in the “data plane” for I/O operations to devices. This
is similar to the way the control plane sets up forwarding tables in Software Defined Networks (SDN).
