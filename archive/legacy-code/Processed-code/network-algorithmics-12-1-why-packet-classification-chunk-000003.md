# network-algorithmics-12-1-why-packet-classification (chunk 000003)

FIGURE 12.1
Example of rules that provide traffic-sensitive routing, a firewall rule, and resource reservation. The first rule routes
video traffic from S1 to D via L1; not shown is the default routing to D, which is via L2. The second rule blocks
traffic from an experimental site, S2, from accidentally leaving the site. The third rule reserves 50 Mbps of traffic
from an internal network X to an external network Y, implemented perhaps by forwarding such traffic to a special
outbound queue that receives special scheduling guarantees; here X and Y are prefixes.

the ISP to a server (or subnetwork) within the ISP. Thus, new offending sources could be discovered
and new servers could be added that need protection. In fact, we speculate that one reason why core
router classifiers are not even bigger is that most core router implementations slow down (and do not
guarantee true wire speed forwarding) as classifier sizes increase.
    Third, after the emergence of SDN and virtualization, packet classification has also become a key
component of software switches especially in hypervisors (Pfaff et al., 2015). The use of server vir-
tualization has resulted in most data center and many enterprise networks becoming virtual networks
that connect virtual ports corresponding to virtual machines. Further, these virtual networks may be
reconfigured rapidly as virtual machines migrate. For example, Open VSwitch allows the switch to be
reprogrammed at rapid rates using an Open Flow controller (Pfaff et al., 2015).
