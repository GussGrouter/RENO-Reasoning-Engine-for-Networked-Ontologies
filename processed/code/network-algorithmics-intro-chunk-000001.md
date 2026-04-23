# Chunk 000001

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 20–21
- From: processed/code/network-algorithmics-intro-p20-24.md

---

Preface

Computer networks have become an integral part of society. We take for granted the ability to transact
commerce over the Internet and that users can avail themselves of a burgeoning set of communication
methods, which range from file sharing to Web logs. However, for networks to take their place as part
of the fundamental infrastructure of society, they must provide performance guarantees.
     We take for granted that electricity will flow when a switch is flicked and that telephone calls
will be routed on Mother’s Day. But the performance of computer networks such as the Internet is
still notoriously unreliable. While there are many factors that go into performance, one major issue
is that of network bottlenecks. There are two types of network bottlenecks: resource bottlenecks and
implementation bottlenecks.
     Resource bottlenecks occur when network performance is limited by the speed of the underlying
hardware; examples include slow processors in server platforms and slow communication links. Re-
source bottlenecks can be worked around, at some cost, by buying faster hardware. However, it is quite
often the case that the underlying hardware is perfectly adequate but that the real bottleneck is a de-
sign issue in the implementation. For example, a Web server running on the fastest processors may
run slowly because of redundant data copying. Similarly, a router with a simple packet classification
algorithm may start dropping packets when the number of ACL rules grows beyond a limit, though it
keeps up with link speeds when classification is turned off. This book concentrates on such network
implementation bottlenecks, especially at servers and routers.
     Beyond servers and routers, new breeds of networking devices that introduce new performance
bottlenecks are becoming popular. As networks become more integrated, devices such as storage area
networks (SANs) and multimedia switches are becoming common. Further, as networks get more com-
plex, various special-purpose network appliances for file systems and security are proliferating. While
the first generation of such devices justified themselves by the new functions they provided, it is be-
coming critical that future network appliances keep up with link speeds.
     Thus the objective of this book is to provide a set of techniques to overcome implementation bottle-
necks at all networking devices and to provide a set of principles and models to help overcome current
and future networking bottlenecks.

Audience
This book was written to answer a need for a text on efficient protocol implementations. The vast
majority of networking books are on network protocols; even the implementation books are, for the
most part, detailed explanations of the protocol. While protocols form the foundation of the field, there
are just a handful of fundamental network infrastucture protocols left, such as TCP and IP. On the other
hand, there are many implementations as most companies and start-ups customize their products to
gain competitive advantage. This is exacerbated by the tendency to place TCP and IP everywhere, from
bridges to SAN switches to toasters.
                                                                                                     xix

---

xx        Preface
