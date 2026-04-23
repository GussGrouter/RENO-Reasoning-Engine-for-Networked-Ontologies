# network-algorithmics-18-4-1-new-abstractions-this-book-dealt-with-the-fast-implementation-of-the-sta (chunk 000002)

overhead. A more speculative approach to reduce DNS lookup times in Web accesses by passing
    hints (P10) is described in Chandranmenon and Varghese (2001).
•   Web services: The notion of Web services, by which a Web page is used to provide a service, is get-
    ting increasingly popular. There are a number of protocols that underly Web services, and standard
    implementations of these services can be slow.
•   CORBA: The common object request broker architecture is popular but quite slow. Gokhale and
    Schmidt (1998) apply to the problem four of the principles described in this book (eliminating waste,
    P1, optimizing the expected case, P11, passing information between layers, P9, and exploiting lo-
    cality for good cache behavior, P4a). They show that such techniques from endnode algorithmics
    can improve the performance of the SunSoft Inter-Orb protocol by a factor of 2–4.5, depending on
    the data type. Similar optimizations should be possible in hardware.
•   SSL and other encryption standards: Many Web servers use the secure socket layer (SSL) for secure
    transactions. Software implementations of SSL are quite slow.
•   XML processing: XML is rapidly becoming the lingua franca of the Web. Parsing and converting
    from XML to HTML can be a bottleneck.
•   Measurement and security abstractions: Currently, SNMP and NetFlow allow very primitive mea-
    surement abstractions. The abstraction level can be raised only by a tool that integrates all the raw
    measurement data. Perhaps in the future routers will have to implement more sophisticated abstrac-
    tions to help in measurement and security analysis.
•   Sensor networks: A sensor network may wish to calculate new abstractions to solve such specific
    problems as finding high concentrations of pollutants and ascertaining the direction of a forest fire.
    If history is any guide, every time an existing bottleneck becomes well studied, a new abstrac-
tion appears with a new bottleneck. Thus after lookups became well understood, packet classification
emerged. After classification came TCP offload; and now SSL and XML are clearly important. Many
pundits believe that wire speed security solutions (as implemented in a router or an intrusion detec-
tion system) will be required by the year 2006. Thus it seems clear that future abstractions will keep
presenting new challenges to network algorithmics.
