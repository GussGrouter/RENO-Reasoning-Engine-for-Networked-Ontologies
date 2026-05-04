# network-algorithmics-18-1-3-toward-a-synthesis-in-his-book-the-character-of-physical-law-richard-fey (chunk 000003)

higher level, could a Web server use worst-case weighted fair queuing to provide better delay bounds for
certain clients? In recent years the two communities (scheduling in routers and scheduling in endnode)
have influenced each other. Today sophisticated endnode scheduling algorithms are implemented in
operating systems such as Linux qdisc (Components of Linux Traffic Control, 2022) and Google’s
carousel (Saeed et al., 2017) described in Chapter 7.
   So far, we have suggested that endnodes could learn from router design in overall I/O architecture
and operating system design. Routers can potentially learn the following from endnodes.
   1. Fundamental Algorithms: Fundamental algorithms for endnodes, such as selection, buffer allo-
cation, CRCs, and timers, are likely to be useful for routers, because the router processor is still an
endnode, with very similar issues.
   2. More Structured Router Operating Systems: While the internals of router operating systems, such
as Cisco’s IOS and Juniper’s JunOS, are hidden from public scrutiny, there is at least anecdotal evidence
that there are major software engineering challenges associated with such systems as time progresses
(leading to the need to be compatible with multiple past versions) and as customers ask for special
builds. Perhaps routers can benefit from some of the design ideas behind existing operating systems
that have stood the test of time.
While protection may be fundamentally unnecessary (no third-party applications running on a router),
how should a router operating system be structured for modularity? One approach to building a modular
but efficient router operating system can be found in the router plugins system (Decasper et al., 1998)
and the Click operating system (Kohler et al., 2000). More modern proposals include Arrakis (Peter et
al., 2015) and (Belay et al., 2016).
   3. Vertically Integrated Routers: The components of an endnode (applications, operating system,
boxes, chips) are often built by separate companies, thus encouraging innovation. The interface be-
tween these components is standardized (e.g., the API between applications and operating system),
allowing multiple companies to supply new solutions. Why should a similar vision not hold for routers
some years from now especially as the vision of Software Defined Networks continues to take hold?
Currently, this is more of a business than a technical issue because the dominant vendors do not want
to open up the market to competitors. However, this was true in the past for computers and is no longer
true; thus there is hope.
We are already seeing router chips being manufactured by semiconductor companies. However, a great
aid to progress would be a standardized router operating system that is serious and general enough for
production use by several, if not all, router companies.1 Such a router operating system would have to
work across a range of router architectures, just as operating systems span a variety of multiprocessor
and disk architectures.
Once this is the case, perhaps there is even a possibility of “applications” that run on routers. This is not
as far-fetched as it sounds, because there could be a variety of security and measurement programs that
operate on a subset of the packets received by the router. With the appropriate API (and especially if
the programs are operating on a logged copy of the router packet stream), such applications could even
be farmed out to third-party application developers. It is probably easy to build an environment where

1 Click is somewhat biased toward endnode bus-based routers as opposed to switch-based routers with ASIC support.

18.2 What network algorithmics is about            519

a third-party application (working on logged packets) cannot harm the main router functions, such as
forwarding and routing.
