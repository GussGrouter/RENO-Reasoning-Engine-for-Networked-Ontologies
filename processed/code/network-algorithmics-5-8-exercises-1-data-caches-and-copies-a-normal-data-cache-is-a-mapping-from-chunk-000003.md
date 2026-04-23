# network-algorithmics-5-8-exercises-1-data-caches-and-copies-a-normal-data-cache-is-a-mapping-from (chunk 000003)

In a Scott Adams cartoon Dilbert complains to Dogbert that he is embarrassed to work at a company
where even paying a simple invoice takes 6 months. The invoice first comes into the mail room for
aging, spends some time at the secretary’s desk, goes to the desk of the main decision maker, and
finally ends up in accounts payable. When processing an invoice in Dilbert’s company, the flow of
control works its way through layers of command, each of which incurs significant overhead.
    A management consultant might suggest that Dilbert’s company streamline the processing of an
invoice by eliminating mediating layers wherever possible and by making each layer as responsive as
possible. However, each layer has some reason for existence. The mailroom aggregates mail delivery
service for all departments in the company. The secretary protects the busy boss from interrupts and
weeds out inappropriate requests. The boss must eventually decide whether the invoice is worth paying.
Finally, the mundane details of disbursing cash are best left to accounts payable.
    A modern CPU processing a network message also goes through similar layers of mediation. The
device, for example, an Ethernet adaptor, interrupts the CPU, asking somewhat stridently for attention.
Control is passed to the kernel. The kernel batches interrupt wherever possible, does the network layer
processing for the packet, and finally schedule the application process (say, a Web server) to run. As
always, the reception of a single packet provides too limited a picture of the overall processing context.
For instance, a Web server will parse the request (such as a GET) in the network packet, look for the
file, and institute proceedings to retrieve the file from disk. When the file gets read into memory, a
response containing the requested file is sent back, prepended with an HTTP header.
    While Chapter 5 concentrated on reducing the overhead of operations that touch the data in a packet
(e.g., copying, checksumming), this chapter concentrates on reducing the control overheads involved in
processing a packet. As in Chapter 5, we start by examining the control overheads involved in sending
or receiving a packet. We then broaden to our canonical network application, a Web server.
    As we said in the introduction to Chapter 5, there have been changes in the underlying technologies,
but not the principles, since the first edition. The most relevant for the purposes of reducing control
overheads are as follows. First, as described in Chapter 5 multicore CPUs are the norm. However, the
issue that concerns us more in this chapter is affinity. How do modern CPUs make sure that that network
processing occurs in the same CPU (or on CPUs that share the same L3 cache) that runs the application?
We describe packet steering mechanisms to affinitize packet processing.
    Second, hypervisors and virtual switches are standard in data centers to improve server utilization.
This adds another layer of control overhead. Thus, new solutions like SRIOV (2018) (Single Root I/O
Virtualization, see later for details) have emerged to bypass these overheads. Third, in the first edition,
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00012-9
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                            145

146       Chapter 6 Transferring control
