# network-algorithmics-13-4-the-take-a-ticket-crossbar-scheduler (chunk 000004)

port 1 broadcasts T 3 (finally!), port 2 broadcasts T 2, and port 3 broadcasts T 1. This results in the final
diagram of the third row, where the crossbar connects A and 3, B and 2, and C and 1.
     The take-a-ticket scheme scales well in the control state, requiring only two (log2 N )-bit counters
at each output port to store the current ticket number being served and the highest ticket number dis-
pensed. This allowed the implementation in DEC’s GigaSwitch to scale easily to 36 ports (Souza et
al., 1994), even in the early 1990s when on-chip memory was limited. The scheme used a distributed
scheduler, with each output port’s arbitration done by a so-called GPI chip per line card; the GPI chips
communicate via a control bus.
     The GPI chips have to arbitrate for the (serial) control bus so as to present a request to an output line
card and to obtain a queue number. Because the control bus is a broadcast bus, an input port can figure
out when its turn comes by observing the service of those who were before it, and it can then instruct
the crossbar to make a connection.
     Besides the small control state, the take-a-ticket scheme has the advantage of being able to handle
variable-sized packets directly. Output ports can asynchronously broadcast the next ticket number when
they finish receiving the current packet; different output ports can broadcast their current ticket numbers
at arbitrary times. Thus unlike all the other schemes described later, there is no header and control
overhead to break up packets into “cells” and then do the reassembly later. On the other hand, take-a-
ticket has limited parallelism because of HOL blocking, a phenomenon we look at in the next section.
     The take-a-ticket scheme also allows a nice feature called hunt groups. Any set of line cards (not
just physically contiguous line cards) can be aggregated to form an effectively higher-bandwidth link
called a hunt group. Thus three 100-Mbps links can be aggregated to look like a 300-Mbps link.
     The hunt group idea requires only small modifications to the original scheduling algorithm because
each of the GPI chips in the group can observe each other’s messages on the control bus and thus keep
local copies of the (common) ticket number consistent. The next packet destined for the group is served
by the first free output port in the hunt group, much as in a delicatessen with multiple servers. While
basic hunt groups can cause reordering of packets sent to different links, a small modification allows
packets from one input to be sent to only one output port in a hunt group via a simple deterministic
hash. This modification avoids reordering, at the cost of reduced parallelism.
     Since the GigaSwitch was a bridge, it had to handle LAN multicast. Because the take-a-ticket
scheduling mechanism uses distributed scheduling via separate GPI chips per output, it is hard to coor-
dinate all schedulers to ensure that every output port is free. Furthermore, waiting for all ports to have
a free ticket for a multicast packet would result in blocking some ports that were ready to service the
packet early, wasting throughput. Hence, multicast was handled by a central processor in software and
was thus accorded “second-class” status.
