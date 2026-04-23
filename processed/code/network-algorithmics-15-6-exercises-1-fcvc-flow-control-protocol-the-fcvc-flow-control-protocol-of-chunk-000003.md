# network-algorithmics-15-6-exercises-1-fcvc-flow-control-protocol-the-fcvc-flow-control-protocol-of (chunk 000003)

Every graduate with a business degree knows that the task of optimizing an organization or process
begins with measurement. Once the bottlenecks in a supply chain are identified and the major cost
factors are outlined, improvements can be targeted. The situation is no different in computer networks.
For example, in service provider networks packet counting and logging provide powerful tools for the
following.
Capacity Planning: Internet service providers (ISPs) need to determine the traffic matrix or the traffic
     between all source and destination subnets they connect. This knowledge can be used on short time
     scales (say, hours) to perform traffic engineering by reconfiguring optical switches; it can also be
     used on longer time scales (say, months) to upgrade link capacity.
Accounting: Internet service providers implement complex service-level agreements (SLAs) with
     customers and peers. Simple accounting arrangements based on overall traffic can easily be mon-
     itored by a single counter; however, more sophisticated agreements based on traffic type require a
     counter per traffic type. Packet counters can also be used to decide peering relationships. Suppose
     ISP A is currently sending packets to ISP C via ISP B and is considering directly connecting (peer-
     ing) with B; a rational way for A to decide is to count the traffic destined to prefixes corresponding
     to B.
Traffic Analysis: Many network managers monitor the relative ratio of one packet type to another. For
     example, a spike in peer-to-peer traffic may require rate limiting. A spike in ICMP messages may
     indicate a Smurf attack.
    Once causes—such as links that are unstable or have excessive traffic—are identified, network op-
erators can take action by a variety of means. Thus measurement is crucial not just to characterize the
network but to better engineer its behavior.
    There are several control mechanisms that network operators currently have at their disposal. For
example, operators can tweak Open Shortest Path First (OSPF) link weights and BGP policy to spread
the load, can set up circuit-switched paths to avoid hot spots, and can simply buy new equipment. This
chapter focuses only on network changes that address the measurement problem—i.e., changes that
make a network more observable. However, we recognize that making a network more controllable,
for instance, by adding more tuning knobs, is an equally important problem we do not address here.
    Despite its importance, traffic measurement, at first glance, does not appear to offer any great
challenges or have much intellectual appeal. As with mopping a floor or washing dishes, traffic mea-
surement appears to be a necessary but mundane chore.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00024-5
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                     449

450      Chapter 16 Measuring network traffic
