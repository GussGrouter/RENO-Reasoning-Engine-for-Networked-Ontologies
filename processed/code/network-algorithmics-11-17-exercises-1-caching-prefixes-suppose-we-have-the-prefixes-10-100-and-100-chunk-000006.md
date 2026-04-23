# network-algorithmics-11-17-exercises-1-caching-prefixes-suppose-we-have-the-prefixes-10-100-and-100 (chunk 000006)

294   Chapter 11 Prefix-match lookups

index= charVariable - ‘a’.

The following definition of a trie node may be helpful.

\#defineALPHA26
  structTRIENODE
  {
  intcompletionStatus;
  charcompletion[MAXLEN];
  structTRIENODE*next[ALPHA];
  }

Can other techniques discussed in the text (e.g., binary search) be applied to this problem? Are
  insertion costs significant?

CHAPTER

Packet classification
                                                                                                             12
                                                                  A classification is a definition comprising a system of definitions.
                                                                                                            —Friedrich von Schlegel

Traditionally, the post office forwards messages based on the destination address in each letter. Thus
all letters to Timbuctoo were forwarded in exactly the same way at each post office. However, to gain
additional revenue, the post office introduced service differentiation between ordinary mail, priority
mail, and express mail. Thus forwarding at the post office is now a function of the destination address
and the traffic class. Further, with the specter of terrorist threats and criminal activity, forwarding could
even be based on the source address, with special screening for suspicious sources.
    In exactly the same way, routers have evolved from traditional destination-based forwarding devices
to what are called packet classification routers. In modern routers, the route and resources allocated to
a packet are determined by the destination address as well as other header fields of the packet, such as
the source address and TCP/UDP port numbers.
    Packet classification unifies the forwarding functions required by firewalls, resource reservations,
QoS routing, unicast routing, and multicast routing. In classification, the forwarding database of a router
consists of a potentially large number of rules on key header fields. A given packet header can match
multiple rules. So each rule is given a cost, and the packet is forwarded using the least-cost matching
rule.
    The world has changed significantly since the first edition, but most of the changes relevant to packet
classification are a subset of the changes described at the start of Chapter 11 on IP lookups. These are the
significant use of IPv6 (which complicates packet classification), the increasing use of Software Defined
Networks (SDN) and hypervisor switches (Pfaff et al., 2015) to do flexible forwarding using packet
classification instead of simpler IP lookups, and the emergence of Network Function Virtualization
(NFV) which requires software solutions to packet classification. We are grateful to Balajee Vamanan
for helping us with more recent work in packet classification. Despite these technological changes, the
essential ideas have remained.
    This chapter is organized as follows. The packet classification problem is motivated in Section 12.1.
The classification problem is formulated precisely in Section 12.2, and the metrics used to evaluate
rule schemes are described in Section 12.3. Section 12.4 presents simple schemes such as linear search,
tuple space search and TCAMs. Section 12.5 begins the discussion of more efficient schemes by de-
scribing an efficient scheme called grid of tries that works only for rules specifying values of only two
fields. Section 12.6 transitions to general rule sets by describing a set of insights into the classification
problem, including the use of a geometric viewpoint.
    Section 12.7 begins the transition to algorithms for the general case with a simple idea to extend 2D
schemes. A general approach based on divide-and-conquer is described in Section 12.8. This is followed
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00019-1
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                                295

296      Chapter 12 Packet classification

Table 12.1 Summary of the principles used in the classification algorithms described in
    this chapter.
    Number                            Principle                                       Lookup technique
    P12         Add marker state                                           Rectangle and tuple search
    P2a         Precompute filter info
    P15         Use Dest and SRC tries                                     Grid of tries
    P2a         Precompute switch pointers
    P15         Divide-and-conquer by first doing field lookups            Bit vector, pruned tuple, cross-producting
    P12, 2a
    P11         Exploit lack of general ranges                             Multiple 2D planes
    P4a         Exploit bitmap memory locality                             Bit vector scheme
    P11         Exploit small number of prefixes that match any field      Pruned tuple
    P11a, 4a    Exploit cross product locality                             On-demand cross product
    P1          Avoid redundant cross products                             Equivalent cross-producting
