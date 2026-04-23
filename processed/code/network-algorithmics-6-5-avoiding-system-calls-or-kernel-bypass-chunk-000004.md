# network-algorithmics-6-5-avoiding-system-calls-or-kernel-bypass (chunk 000004)

9 This is a way of avoiding packet filters completely by passing more information in packets, but it is a bit scary in a networking
environment because of the security risks; however, it is typically used only within clusters of machines that trust each other.

6.5 Avoiding system calls or Kernel Bypass               169

only small messages or (large) block transfer. The fast messages implementation (Pakin et al., 1997)
goes further to combine user-level scatter–gather interfaces and flow control to enable uniform high
performance for a continuum from short to long messages.

What are kernels good for?
It is important to consider this question because the ADC and active message approaches bypass the
kernel. Kernels are good for protection (protecting the system and good users from malice or errors)
and for scheduling resources among different applications. Thus if we remove the kernel from the run-
time data path, it is up to the solution to provide these services in lieu of the kernel. For example, ADCs
do protection using the virtual memory hardware (to protect descriptors) and adaptor enforcement (to
protect buffer memory).
     It also must multiplex the physical communication link (especially on the sending side) among the
different ADCs and provide some sort of fairness. To do this in every device would require replicating
traditional kernel code in every device; however, it can be argued that some devices, such as the disk
and the network adaptor, are special in terms of their performance needs and are worth giving special
treatment. The first commercial deployment of the ADC idea and the UUNET solution (similar to
ADCs and proposed concurrently) advocated at Cornell (von Eicken et al., 1995) was known as the
Virtual Interface Architecture (VIA). We briefly describe VIA and then move on to the modern version
called DPDK (2018) that is widely deployed.
