# network-algorithmics-9-4-reassembly-both-header-prediction-for-tcp-and-even-the-udp-optimizations (chunk 000002)

The current Internet strategy (Kent and Mogul, 1987) is to shift the fragmentation computation in
space (P3c) from the router and the receiver to the sender. The idea behind the so-called path MTU
scheme is that the onus falls on the sender to compute a packet size that is small enough to pass through
all links in the path from sender to receiver. Routers can now refuse to fragment a packet, sending back
a control message to the receiver. The sender uses a list of common packet sizes (P11, optimizing the
expected case) and works its way down this list when it receives a refusal.
     The path MTU scheme nicely illustrates algorithmics in action by removing a problem by moving
to another part of the system. However, a misconception has arisen that path MTU has completely
removed fragmentation in the Internet. This is not so. Almost all core routers support fragmentation in
hardware, and a significant amount of fragmented traffic has been observed (Shannon et al., 2001) on
Internet backbone links many years after the path MTU protocol was deployed.
     Note that the path MTU protocol requires the sender to keep state, typically in PCB, as to the best
current packet size to use. This works well if the sender uses TCP, but not if the sender uses UDP, which
is stateless. In the case of UDP path MTU can be implemented only if the application above UDP keeps
the necessary state and implements path MTU (unless the path MTU is stored as a routing table entry
like in an IBM AIX system). This is harder to deploy because it is harder to change many applications,
unlike changing just TCP. Thus at the time of writing, shared file system protocols such as NFS, IP
within IP encapsulation protocols, and many media player and game protocols run over UDP and do
not support path MTU. Finally, many attackers compromise security by splitting an attack payload
across multiple fragments. Thus intrusion detection devices must often reassemble IP fragments to
check for suspicious strings within the reassembled data.
     Thus it is worth investigating fast reassembly algorithms because common programs such as NFS
do not support the path MTU protocol and because real-time intrusion detection systems must reassem-
ble packets at line speeds to detect attacks hidden across fragments. The next section describes fast
reassembly implementations at receivers.
