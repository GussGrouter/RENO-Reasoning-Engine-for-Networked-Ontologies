# network-algorithmics-7-11-exercises-1-better-hash-functions-currently-hashed-wheels-use-a-very-sim (chunk 000002)

A protocol, like a copy center or an ice cream parlor, should be able to serve multiple clients. The
clients of a protocol could be end-users (as in the case of the file transfer protocol), software programs
(for example, when the tool traceroute uses the Internet protocol), or even other protocols (as in the
case of the email protocol SMTP, which uses TCP).
    Thus when a message arrives, the receiving protocol must dispatch the received message to the
appropriate client. This function is called demultiplexing. Demultiplexing is an integral part of data link,
routing, and transport protocols. It is a fundamental part of the abstract protocol model of Chapter 2.
    Traditionally, demultiplexing is done layer by layer using a demultiplexing field contained in each
layer header of the received message. Called layered demultiplexing, this is shown in Fig. 8.1. For ex-
ample, working from bottom to top in the picture, a packet may arrive on the Ethernet at a workstation.
The packet is examined by the Ethernet driver, which looks at a so-called protocol type field to decide
what routing protocol (e.g., IP, IPX) is being used. Assuming the type field specifies IP, the Ethernet
driver may upcall the IP software.
    After IP processing, the IP software inspects the protocol ID field in the IP header to determine
the transport protocol (e.g., TCP or UDP?). Assuming it is TCP, the packet will be passed to the TCP
software. After doing TCP processing, the TCP software will examine the port numbers in the packet
to demultiplex the packet to the right client, say, to a process implementing HTTP.
    Traditional demultiplexing is fairly straightforward because each layer essentially does an exact
match on some field or fields in the layer header. This can be done easily, using, say, hashing, as we
describe in Chapter 10. Of course, the lookup costs add up at each layer.
    By contrast, this chapter concentrates on early demultiplexing, which is a much more challenging
task at high speeds. Referring back to Fig. 8.1, early demultiplexing determines the entire path of
protocols taken by the received packet in one operation when the packet first arrives. In the last example
early demultiplexing would determine in one fell swoop that the path of the Web packet was Ethernet,
IP, TCP, Web. A possibly better term is layered demultiplexing. However, this book uses the more
accepted name of early demultiplexing.
    What makes early demultiplexing hard in general is to also allow applications to flexibly specify the
lower layer protocols they wish to run over or whose packets they wish to receive. This is particularly
useful for traffic monitoring or security applications. However, if the early demultiplexing is confined
to TCP connections that have become standard in the last 20 years, the problem is much simpler and
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00014-2
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                   195

196       Chapter 8 Demultiplexing

FIGURE 8.1
Traditional layered demultiplexing has each layer demultiplex a packet to the next layer software above using a field
in the layer header.
